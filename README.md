
# Système de Gestion de Réservations

Découvrez le **Système de Gestion de Réservations**, un exemple d'intégration des **Modèles de Langage (LLMs)** dans des applications réelles. Grâce à **Ollama**, ce système offre des recommandations personnalisées et facilite la gestion interactive des réservations de vol.

## Fonctionnalités Principales

- **Recherche de Réservations :** Récupérez vos réservations en entrant votre numéro de réservation.
- **Suggestions de Lieux à Visiter :** Recevez des recommandations sur les endroits à visiter à votre destination grâce à l'IA Ollama.
- **Modification des Réservations :** Changez votre destination et/ou votre date de vol avec des confirmations avant sauvegarde.

## Prérequis

Avant de commencer, assurez-vous d'avoir :

- **Python 3.7 ou supérieur** installé.
- **Packages Python :** `pandas`, `langchain_community`
- **Ollama Language Model :** Installez et configurez Ollama. [Documentation Ollama](https://ollama.com/docs)

## Installation

1. **Cloner le Répertoire**

   ```bash
   git clone https://github.com/votreutilisateur/systeme-gestion-reservations.git
   cd systeme-gestion-reservations
   ```

## Utilisation

Lancez le script via la ligne de commande :
   ```bash
   python3 manage_reservations.py
   ```

## Suivre les Instructions

Entrer le Numéro de Réservation : Fournissez votre numéro de réservation (ex. ABC123).
Voir les Détails : Le système affichera les détails de votre réservation actuelle ainsi que des suggestions de lieux à visiter.
Modifier la Destination : Sélectionnez une nouvelle destination parmi les options proposées.
Confirmer la Destination : Après sélection, confirmez si vous souhaitez définir la nouvelle destination.
Modifier la Date de Vol : Choisissez une nouvelle date de vol parmi les options disponibles.
Confirmer et Sauvegarder : Confirmez les modifications pour les enregistrer dans le fichier reservations_updated.csv.

## Exemple de Sortie

Voici un exemple d'interaction avec le script démontrant ses capacités :
```md
$ python3 manage_reservations.py
Veuillez entrer votre numéro de réservation : ABC123

**Réservation trouvée :**
ReservationNumber: ABC123
Name: John Doe
Destination: Singapore
Region: Singapore
FlightDate: 2024-10-30

**Suggestions de lieux à visiter à Singapore :**

Singapore est un archipel multiculturel situé dans le Sud-Est asiatique qui offre une expérience touristique unique en raison de sa diversité culturelle, gastronomique et architecturale. Voici quelques-uns des endroits les plus intéressants à visiter à Singapour :

1.  **Gardens by the Bay** : Un parc botanique innovant situé dans le district de Marina East. Gardens by the Bay est célèbre pour ses jardins supérieurs, qui incluent la « Supertree Grove », une collection d'arbres géants avec des illuminations nocturnes et un espace vert appelé « Cloud Forest ».
2.  **Marina Bay Sands SkyPark** : Un observatoire situé au sommet du complexe hôtelier Marina Bay Sands, offrant une vue imprenable sur la ville.
3.  **Merlion Park** : Situé dans le district de Marina Bay, il est célèbre pour son statue géante du Merlion, qui symbolise Singapour et est un symbole emblématique de la ville.
4.  **Sentosa Island** : Une île située à l'ouest de Singapour, Sentosa Island est connue pour ses plages, ses parcs d'amusement et son aquarium.
5.  **Chinatown** : Le quartier chinois de Singapour, Chinatown est un endroit animé où vous pouvez trouver des magasins, des restaurants et des marchés locaux.
6.  **Clarke Quay** : Un quartier très animé situé dans le district de Riverside, Clarke Quay offre une vue imprenable sur la rivière Singapour et propose diverses activités nocturnes telles que des bars, des clubs et des restaurants.
7.  **National Gallery Singapore** : Un musée d'art contemporain qui présente l'histoire de l'art en Asie du Sud-Est.
8.  **Sungei Buloh Wetland Reserve** : Situé dans le district de Yishun, il est célèbre pour ses zones humides et son importance pour la conservation des oiseaux migrateurs.
9.  **Singapore Botanic Gardens** : Un jardin botanique qui abrite plus de 10 000 espèces de plantes différentes, y compris le célèbre Jardin National Orchid.
10. **Little India** : Le quartier indien de Singapour, Little India est connu pour ses magasins, ses restaurants et son marché local animé.

Voulez-vous définir 'Bangkok' comme nouvelle destination ? (oui/non) : oui

Veuillez choisir une nouvelle date de vol parmi les options suivantes :
1. 2024-10-30
2. 2024-11-12
3. 2024-12-01
Entrez le numéro correspondant à votre choix de date de vol (1-3), ou tapez 'aide' pour plus d'informations : 1
Voulez-vous sauvegarder ces modifications ? (oui/non) : oui

Réservation ABC123 modifiée avec succès.

Les réservations ont été sauvegardées dans 'reservations_updated.csv'.
```
