
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
Region: Singapour
FlightDate: 2024-10-30

**Suggestions de lieux à visiter à Singapore :**

Singapore est un paradis pour les voyageurs en raison de sa richesse culturelle, du mélange fascinant de traditions asiatiques et occidentales, ainsi que de son environnement urbain exceptionnellement propre et bien organisé.

**1. Jardin botanique de Singapour**

L'un des jardins botaniques les plus impressionnants au monde, le jardin botanique de Singapour abrite une grande diversité d'espèces végétales. Les visiteurs peuvent explorer différentes zones telles que la serre climatique, l'arboretum et le jardin tropical, qui offrent un aperçu des écosystèmes naturels du monde entier.

Activités recommandées : Se promener dans les jardins, visiter la serre climatique pour découvrir des plantes rares, profiter de la bibliothèque botanique.

**2. Merlion Park**

Le Merlion est l'emblème national de Singapour et représente un lion avec une tête humaine qui regarde vers l'eau. Le parc offre une vue imprenable sur le lac et la ville, ainsi qu'un aperçu du merlion lui-même. Ce spot idéal pour les photos.

Activités recommandées : Prendre des photos avec le Merlion, se promener autour du lac, profiter de la vue panoramique sur Singapour.

**3. Chinatown**

Le quartier chinois de Singapour est l'un des plus grands et des plus animés d'Asie du Sud-Est. Il offre une expérience culturelle riche avec ses rues étroites, ses temples, ses restaurants et ses magasins de souvenirs.

Activités recommandées : Visiter le temple de Thian Hock Keng, explorer les ruelles pour découvrir des boutiques et des restaurants locaux, profiter de la nourriture chinoise dans l'un des nombreux restaurants.

**4. Marina Bay Sands**

Ce complexe hôtelier est célèbre en raison de son observation tower, qui offre une vue imprenable sur Singapour. Le complexe comprend également un centre commercial, un casino et plusieurs options de restauration.

Activités recommandées : Se rendre au sommet du tour pour admirer la vue panoramique, explorer le centre commercial pour faire du shopping ou profiter d'un repas à l'une des restaurants.

**5. Gardens by the Bay**

Ces jardins sont un spectacle à ne pas manquer avec ses arbres gigantesques et ses sculptures de lumière. Les visiteurs peuvent explorer les différents districts, notamment la «Supertree Grove», qui propose une expérience unique et des vues incroyables.

Activités recommandées : Se promener dans les jardins pour admirer les arbres et les sculptures lumineuses, visiter l'«OCBC Skyway» pour profiter d'une vue panoramique de la zone.

**6. Sentosa Island**

Cette île est un paradis pour ceux qui cherchent à se détendre ou à s'amuser. Elle comprend des plages, des parcs aquatiques, des casinos et des restaurants.

Activités recommandées : Se promener sur les plages de Siloso et Palawan, visiter S.E.A. Aquarium, profiter d'une journée aux Universal Studios Singapore.

**7. Haw Par Gardens**

Ces jardins sont un site historique important, célèbre pour ses sculptures qui racontent des légendes chinoises et hindoues. Les visiteurs peuvent explorer les différentes scènes sculptées qui décrivent la vie après la mort.

Activités recommandées : Explorer les jardins pour découvrir les sculptures et les légendes qu'elles représentent, visiter le musée pour en savoir plus sur l'histoire des jardins.

**8. Clarke Quay**

Ce quartier est un endroit animé de Singapour où les visiteurs peuvent profiter d'une variété d'options de restauration, de bars et de musique live. C'est également un excellent spot pour faire du shopping ou simplement se promener le long de la rivière.

Activités recommandées : Se promener dans le quartier pour découvrir des boutiques et des restaurants locaux, prendre part à une soirée animée avec de la musique live et des bars.

**9. National Gallery Singapore**

Ce musée est consacré aux arts modernes et contemporains d'Asie. Les visiteurs peuvent explorer les différentes expositions temporaires qui mettent en avant l'œuvre de différents artistes du continent.

Activités recommandées : Visiter le musée pour découvrir des œuvres d'art modernes et contemporaines, participer à des événements culturels et éducatifs organisés par le musée.

**10. Hume Road Market**

Ce marché est un endroit idéal pour ceux qui cherchent à acquérir des produits locaux ou à manger de la nourriture chinoise. Les visiteurs peuvent y trouver une variété d'articles, du jus de fruits frais jusqu'à des vêtements.

Activités recommandées : Se promener dans le marché pour découvrir les différents articles et les options de restauration, profiter de la nourriture locale et des produits locaux.

En conclusion, Singapour offre un mélange unique d'expériences culturelles, de divertissement et de détente. Les endroits que j'ai mentionnés ci-dessus offrent une bonne base pour commencer votre exploration de cette ville fascinante.

Veuillez choisir une nouvelle destination parmi les options suivantes :
1. Bangkok
2. Singapore
3. Tokyo
Entrez le numéro correspondant à votre choix de destination (1-3), ou tapez 'aide' pour plus d'informations : 1

**Suggestions de lieux à visiter à Bangkok :**

**Suggestions de lieux à visiter à Bangkok :**

Bangkok est la capitale de la Thaïlande et se situe au centre du pays. Cette ville est un mélange unique d'architecture traditionnelle thaïe, de temples anciens et de centres commerciaux modernes.

### 1. Grand Palais
Le Grand Palais (Grand Palace) est l'un des sites les plus emblématiques de Bangkok et une attraction incontournable pour tout voyageur. Situé dans le cœur de la ville, il a été la résidence officielle du roi de Thaïlande pendant près d'un siècle. Le palais abrite de nombreux temples (wat), des bâtiments administratifs et un musée qui mettent en valeur l'histoire et les traditions royales thaïlandaises.

Activités recommandées : Visitez le temple de la Démone Blanche, le temple du Bouddha d'Or et explorez les jardins et les cours intérieures. Profitez également des spectacles traditionnels qui ont lieu régulièrement au palais.
Points d'intérêt principaux : Le Grand Palais lui-même est un point d'intérêt majeur, mais il est aussi célèbre pour ses temples et ses jardins.

### 2. Wat Phra Kaew
Wat Phra Kaew, situé dans le complexe du Grand Palais, est une autre attraction incontournable de Bangkok. Ce temple royal abrite la précieuse statue d'Emeraude Bouddha, qui est considérée comme l'un des plus grands trésors religieux du monde.

Activités recommandées : Visitez la salle où se trouve le Bouddha d'Emeraude et admirez les détails architecturaux et artistiques de ce temple.
Points d'intérêt principaux : La statue d'Emeraude Bouddha est un point d'intérêt principal, mais les mosaïques et les peintures murales du temple sont également dignes d'être vues.

### 3. Wat Arun
Wat Arun, situé sur la rive gauche de la Chao Phraya River, est un autre site sacré de Bangkok. Il est célèbre pour sa tour dorée qui brille au-dessus des autres bâtiments du temple.

Activités recommandées : Montez dans la tour pour admirer les vues panoramiques sur le fleuve et explorez les jardins et les cours intérieures du temple.
Points d'intérêt principaux : La tour dorée de Wat Arun est un point d'intérêt principal, mais l'architecture et les détails artistiques du temple sont également dignes d'être vus.

### 4. Musée National de Bangkok
Le Musée National de Bangkok (Museum Siam) est une attraction qui offre une expérience unique en mettant en valeur l'histoire de la capitale thaïlandaise. Le musée utilise des méthodes interactives pour présenter les aspects culturels, historiques et sociaux de Bangkok.

Activités recommandées : Explorez les expositions sur l'histoire de Bangkok, visitez les salles qui abritent des objets d'intérêt culturel et profitez du centre d'interprétation numérique.
Points d'intérêt principaux : Les expositions interactives sont un point d'intérêt principal, mais le musée lui-même est une attraction valable.

### 5. Quartier de Banglamphu
Banglamphu est l'un des quartiers historiques les plus anciens et les plus emblématiques de Bangkok. Il abrite de nombreux temples, marchés traditionnels et rues commerçantes qui offrent une expérience unique du patrimoine culturel thaïlandais.

Activités recommandées : Explorez les rues étroites pour découvrir des boutiques d'artisanat local, visitez le temple de Kuan Yin, un grand temple bouddhiste féminin, et profitez des plats locaux dans les restaurants traditionnels.
Points d'intérêt principaux : Le quartier lui-même est un point d'intérêt principal, mais les temples, les marchés et les rues commerçantes sont également dignes d'être vues.

En résumé, Bangkok offre une richesse culturelle, historique et architecturale unique qui en fait un lieu de voyage incontournable. Ces endroits à visiter offrent des expériences variées allant du patrimoine sacré aux centres culturels modernes, offrant à chaque visiteur l'opportunité d'explorer le cœur de la capitale thaïlandaise.
Voulez-vous définir 'Bangkok' comme nouvelle destination ? (oui/non) :

Veuillez choisir une nouvelle date de vol parmi les options suivantes :
1. 2024-10-30
2. 2024-11-12
3. 2024-12-01
Entrez le numéro correspondant à votre choix de date de vol (1-3), ou tapez 'aide' pour plus d'informations : 1
Voulez-vous sauvegarder ces modifications ? (oui/non) : oui

Réservation ABC123 modifiée avec succès.

Les réservations ont été sauvegardées dans 'reservations_updated.csv'.
```
