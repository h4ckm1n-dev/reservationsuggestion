
# Gestion de Réservations

Ce projet permet de simuler la gestion de réservations de vols à partir d'un fichier CSV. Il permet de rechercher, modifier et sauvegarder des réservations.

## Fonctionnalités

- **Recherche de réservation** : Trouvez une réservation par son numéro.
- **Modification de réservation** : Changez la date de vol ou la destination d'une réservation.
- **Sauvegarde des modifications** : Mettez à jour et sauvegardez les nouvelles informations dans le fichier CSV.

## Fichiers

- `reservations.csv` : Contient les données de réservation.
- `manage_reservations.py` : Script Python pour gérer les réservations.

## Exemple d'utilisation

1. **Charger les réservations** :
   Le fichier `reservations.csv` contient les réservations à gérer.

2. **Modifier une réservation** :
   Le script modifie la réservation avec le numéro `ABC123` en changeant la date et la destination.

3. **Sauvegarder les modifications** :
   Les modifications sont ensuite sauvegardées dans le fichier CSV.

## Exécution

Pour exécuter le script, suivez les étapes suivantes :

```bash
# Cloner le dépôt
git clone https://github.com/votre-utilisateur/GestionReservations.git
cd GestionReservations

# Exécuter le script
python manage_reservations.py
```

## Licence

Ce projet est sous licence MIT.
