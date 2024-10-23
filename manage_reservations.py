import pandas as pd
from langchain_community.llms import Ollama
import re  # Pour la validation et le nettoyage des entrées
import sys  # Pour quitter le programme gracieusement

# Initialiser le LLM sans max_tokens
llm = Ollama(model="llama3.1", temperature=0.5)

# Mapping de Destination à Région (optionnel, peut être utilisé pour des suggestions contextuelles)
DESTINATION_TO_REGION = {
    'Bangkok': 'Thaïlande',
    'Singapore': 'Singapour',
    'Tokyo': 'Japon',
    # Ajouter d'autres mappings si nécessaire
}

# Charger les réservations depuis un fichier CSV
def load_reservations(file_path):
    try:
        reservations = pd.read_csv(file_path)
        required_columns = {'ReservationNumber', 'Name', 'FlightDateID', 'DestinationID'}
        if not required_columns.issubset(reservations.columns):
            raise ValueError(f"Le fichier de réservations doit contenir les colonnes {required_columns}.")
        return reservations
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{file_path}' n'a pas été trouvé.")
        sys.exit(1)
    except Exception as e:
        print(f"Erreur lors du chargement des réservations : {e}")
        sys.exit(1)

# Charger les destinations depuis un fichier CSV
def load_destinations(file_path):
    try:
        destinations = pd.read_csv(file_path)
        required_columns = {'DestinationID', 'Destination'}
        if not required_columns.issubset(destinations.columns):
            raise ValueError(f"Le fichier des destinations doit contenir les colonnes {required_columns}.")
        return destinations
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{file_path}' n'a pas été trouvé.")
        sys.exit(1)
    except Exception as e:
        print(f"Erreur lors du chargement des destinations : {e}")
        sys.exit(1)

# Charger les dates de vol depuis un fichier CSV
def load_dates(file_path):
    try:
        dates = pd.read_csv(file_path)
        if {'FlightDateID', 'FlightDate'}.issubset(dates.columns):
            return dates
        else:
            raise ValueError("Le fichier des dates doit contenir les colonnes 'FlightDateID' et 'FlightDate'.")
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{file_path}' n'a pas été trouvé.")
        sys.exit(1)
    except Exception as e:
        print(f"Erreur lors du chargement des dates : {e}")
        sys.exit(1)

# Créer un dictionnaire mappant DestinationID à Destination
def create_destinations_dict(destinations_df):
    return destinations_df.set_index('DestinationID')['Destination'].to_dict()

# Créer des mappings pour les dates de vol
def create_flight_date_mappings(dates_df):
    id_to_date = pd.Series(dates_df.FlightDate.values, index=dates_df.FlightDateID).to_dict()
    date_to_id = pd.Series(dates_df.FlightDateID.values, index=dates_df.FlightDate).to_dict()
    return id_to_date, date_to_id

# Trouver une réservation par numéro de réservation
def find_reservation(reservations, reservation_number, destinations_dict, id_to_date):
    reservation = reservations[reservations['ReservationNumber'] == reservation_number]
    if reservation.empty:
        return None
    else:
        reservation_info = reservation.to_dict(orient='records')[0]
        destination_id = reservation_info['DestinationID']
        destination_name = destinations_dict.get(destination_id, "Destination inconnue")
        region = DESTINATION_TO_REGION.get(destination_name, None)
        flight_date_id = reservation_info['FlightDateID']
        flight_date = id_to_date.get(flight_date_id, "Date inconnue")
        # Mettre à jour reservation_info avec Destination, Région et FlightDate
        reservation_info.update({
            'Destination': destination_name,
            'Region': region,
            'FlightDate': flight_date
        })
        return reservation_info

# Modifier la réservation (changer la date de vol ou la destination)
def modify_reservation(reservations, reservation_number, new_date_id=None, new_destination_id=None):
    if reservation_number in reservations['ReservationNumber'].values:
        if new_date_id:
            reservations.loc[reservations['ReservationNumber'] == reservation_number, 'FlightDateID'] = new_date_id
        if new_destination_id:
            reservations.loc[reservations['ReservationNumber'] == reservation_number, 'DestinationID'] = new_destination_id
        print(f"\nRéservation {reservation_number} modifiée avec succès.")
    else:
        print("\nNuméro de réservation non trouvé.")

# Sauvegarder les changements dans un nouveau fichier CSV
def save_reservations_to_new_file(reservations, file_path):
    try:
        reservations.to_csv(file_path, index=False)
        print(f"\nLes réservations ont été sauvegardées dans '{file_path}'.")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde des réservations : {e}")

# Obtenir le numéro de réservation de l'utilisateur avec validation de base
def get_reservation_number():
    while True:
        reservation_number = input("Veuillez entrer votre numéro de réservation : ").strip()
        if re.match(r'^[A-Za-z0-9]+$', reservation_number):
            return reservation_number
        else:
            print("Numéro de réservation invalide. Veuillez entrer uniquement des caractères alphanumériques.")

# Afficher les options et obtenir le choix de l'utilisateur
def get_user_choice(choices, choice_type):
    while True:
        print(f"\nVeuillez choisir une nouvelle {choice_type} parmi les options suivantes :")
        for idx, choice in enumerate(choices, start=1):
            print(f"{idx}. {choice}")
        user_input = input(f"Entrez le numéro correspondant à votre choix de {choice_type} (1-{len(choices)}), ou tapez 'aide' pour plus d'informations : ").strip()
        
        if user_input.lower() == 'aide':
            # Utilisation du LLM pour fournir plus d'informations sur les choix
            prompt = f"Donne-moi une brève description des différentes options de {choice_type} disponibles."
            try:
                response = llm.generate([prompt], max_tokens=150)  # Transmission de max_tokens ici
                description = response.generations[0][0].text.strip()
                print(f"\n{description}\n")
            except Exception as e:
                print(f"Erreur lors de la génération de l'aide : {e}")
            continue  # Re-afficher les options après avoir fourni de l'aide

        try:
            choice_num = int(user_input)
            if 1 <= choice_num <= len(choices):
                return choice_num - 1  # Retourner l'index basé sur zéro
            else:
                print(f"Choix invalide : {user_input}. Veuillez entrer un nombre entre 1 et {len(choices)}.")
        except ValueError:
            print(f"Entrée non valide : {user_input}. Veuillez entrer un nombre ou 'aide'.")

# Utiliser le LLM pour fournir des suggestions de lieux à visiter
def get_place_suggestions(destination):
    if not destination:
        print("La destination n'est pas disponible.")
        return
    
    # Construire le prompt pour le LLM
    prompt = (
        f"En tant qu'assistant de voyage, suggère des endroits intéressants à visiter à {destination}. "
        "Fournis une brève description de chaque endroit, y compris des activités recommandées et des points d'intérêt principaux."
    )
    
    # Générer les suggestions de lieux en utilisant le LLM
    try:
        response = llm.generate([prompt], max_tokens=500)  # Transmission de max_tokens ici
        suggestions = response.generations[0][0].text.strip()
        
        # Vérifier si la réponse contient un refus
        if "je ne peux pas" in suggestions.lower():
            print("\nDésolé, je ne peux pas générer des suggestions pour le moment.\n")
            # Optionnel : Fournir des suggestions par défaut ou des recommandations générales
        else:
            print(f"\n**Suggestions de lieux à visiter à {destination} :**\n")
            print(suggestions)
    except Exception as e:
        print(f"Erreur lors de la génération des suggestions : {e}")

# Demander la confirmation de l'utilisateur
def confirm_changes():
    while True:
        confirmation = input("Voulez-vous sauvegarder ces modifications ? (oui/non) : ").strip().lower()
        if confirmation in ['oui', 'o']:
            return True
        elif confirmation in ['non', 'n']:
            return False
        else:
            print("Entrée invalide. Veuillez répondre par 'oui' ou 'non'.")

# Exemple d'utilisation
if __name__ == "__main__":
    # Charger les fichiers CSV
    reservations = load_reservations('reservations.csv')
    destinations_df = load_destinations('destinations.csv')
    dates_df = load_dates('dates.csv')
    
    # Créer des dictionnaires pour une recherche facile
    destinations_dict = create_destinations_dict(destinations_df)
    id_to_date, date_to_id = create_flight_date_mappings(dates_df)
    
    # Étape 1 : Obtenir le numéro de réservation de l'utilisateur
    reservation_number = get_reservation_number()
    reservation = find_reservation(reservations, reservation_number, destinations_dict, id_to_date)
    
    if reservation is not None:
        print("\n**Réservation trouvée :**")
        print(f"ReservationNumber: {reservation.get('ReservationNumber')}")
        print(f"Name: {reservation.get('Name')}")
        print(f"Destination: {reservation.get('Destination')}")
        print(f"Region: {reservation.get('Region')}")
        print(f"FlightDate: {reservation.get('FlightDate')}")
        
        # Étape 1.1 : Obtenir des suggestions de lieux à visiter
        get_place_suggestions(reservation.get('Destination'))
    
        # Initialiser une boucle pour sélectionner une nouvelle destination
        while True:
            # Étape 2 : L'utilisateur sélectionne une nouvelle destination
            destinations = destinations_df['Destination'].tolist()
            new_destination_index = get_user_choice(destinations, "destination")
            new_destination = destinations[new_destination_index]
            new_destination_id = destinations_df.iloc[new_destination_index]['DestinationID']
            
            # Étape 3 : Générer de nouvelles suggestions pour la nouvelle destination
            print(f"\n**Suggestions de lieux à visiter à {new_destination} :**")
            get_place_suggestions(new_destination)
            
            # Étape 4 : Demander la confirmation de la nouvelle destination
            while True:
                confirm_dest = input(f"Voulez-vous définir '{new_destination}' comme nouvelle destination ? (oui/non) : ").strip().lower()
                if confirm_dest in ['oui', 'o']:
                    destination_confirmed = True
                    break
                elif confirm_dest in ['non', 'n']:
                    destination_confirmed = False
                    break
                else:
                    print("Entrée invalide. Veuillez répondre par 'oui' ou 'non'.")
            
            if destination_confirmed:
                # Étape 5 : L'utilisateur sélectionne une nouvelle date de vol
                flight_dates = dates_df['FlightDate'].tolist()
                new_flight_date_index = get_user_choice(flight_dates, "date de vol")
                new_flight_date = flight_dates[new_flight_date_index]
                new_flight_date_id = date_to_id.get(new_flight_date)
                
                # Étape 6 : Demander la confirmation avant de sauvegarder les modifications
                if confirm_changes():
                    # Modifier la réservation avec les nouvelles informations
                    modify_reservation(
                        reservations, 
                        reservation_number, 
                        new_date_id=new_flight_date_id, 
                        new_destination_id=new_destination_id
                    )
                    
                    # Sauvegarder les modifications dans un nouveau fichier CSV
                    save_reservations_to_new_file(reservations, 'reservations_updated.csv')
                    break  # Quitter la boucle après sauvegarde
                else:
                    print("\nLes modifications n'ont pas été sauvegardées.")
                    # Optionnel : Demander à l'utilisateur s'il souhaite réessayer ou quitter
                    while True:
                        retry = input("Voulez-vous choisir une nouvelle destination et date ? (oui/non) : ").strip().lower()
                        if retry in ['oui', 'o']:
                            break  # Sortir de la boucle interne pour choisir à nouveau
                        elif retry in ['non', 'n']:
                            print("\nLes modifications n'ont pas été sauvegardées.")
                            sys.exit(0)  # Quitter le script
                        else:
                            print("Entrée invalide. Veuillez répondre par 'oui' ou 'non'.")
            else:
                # L'utilisateur n'a pas confirmé la destination, permettre de choisir à nouveau ou quitter
                while True:
                    retry = input("Voulez-vous choisir une nouvelle destination ? (oui/non) : ").strip().lower()
                    if retry in ['oui', 'o']:
                        break  # Sortir de la boucle interne pour choisir à nouveau
                    elif retry in ['non', 'n']:
                        print("\nAucune modification n'a été effectuée.")
                        sys.exit(0)  # Quitter le script
                    else:
                        print("Entrée invalide. Veuillez répondre par 'oui' ou 'non'.")
    else:
        print(f"\nAucune réservation trouvée pour le numéro : {reservation_number}")

