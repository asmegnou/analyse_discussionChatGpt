# Visualisation des Conversations Sémantiques

Ce projet permet d’analyser et de visualiser des conversations exportées depuis une application de chat. Il utilise des **embeddings sémantiques** pour calculer la similarité entre les conversations et crée un **graphe interactif** avec PyVis.

---

## Fonctionnalités

1. **Chargement des données**
   - Le fichier `conversations.json` contient toutes les conversations exportées.
   - Tu peux obtenir ce fichier en **exportant les données** depuis ton application de chat.

2. **Extraction des titres et messages**
   - Les titres et les messages sont extraits et regroupés dans un `DataFrame` Pandas.
   - Les conversations vides sont ignorées.

3. **Calcul des embeddings sémantiques**
   - Utilisation du modèle `all-MiniLM-L6-v2` de `SentenceTransformer`.
   - Détection automatique du device disponible :
     - GPU Apple (MPS)
     - GPU NVIDIA (CUDA)
     - CPU

4. **Calcul de la similarité**
   - Calcul des similarités cosinus entre toutes les conversations.

5. **Création du graphe interactif avec PyVis**
   - Chaque conversation devient un **nœud**.
   - Les nœuds sont reliés par des **arêtes** si la similarité dépasse un seuil (par défaut `0.5`).
   - Le graphe peut être exploré dans un navigateur web.

6. **Export**
   - Le graphe est généré dans un fichier HTML :  
     ```
     graphe_conversations_semantique.html
     ```
   - Il suffit de l’ouvrir dans un navigateur pour visualiser les conversations et leurs liens sémantiques.

---

## Installation

1. Cloner le projet :
```bash
git clone <URL_DU_REPO>
cd <nom_du_dossier>

    Créer un environnement virtuel et l’activer :

python -m venv venv
source venv/bin/activate    # Linux/macOS
# ou
venv\Scripts\activate       # Windows

    Installer les dépendances :

pip install -r requirements.txt

    Exemple de dépendances :

    pandas
    pyvis
    sentence-transformers
    torch

Utilisation

    Placer le fichier conversations.json dans le dossier du projet.

    Lancer le script Python :

python main.py

    Ouvrir le fichier graphe_conversations_semantique.html dans un navigateur pour explorer le graphe.

Paramètres

    Nombre de conversations : Limité par défaut à 500 pour des raisons de performance (df.head(500)).

    Seuil de similarité : Ajustable dans le script (threshold = 0.5). Plus il est élevé, moins d’arêtes seront créées.

    Longueur des titres et messages : Les titres et messages sont tronqués pour l’affichage (textwrap.shorten).

Technologies utilisées

    Python

Pandas

PyVis

SentenceTransformers

PyTorch
Notes

    Le fichier conversations.json peut être exporté depuis votre application de chat.

    Le graphe généré est interactif et permet de naviguer facilement entre les conversations similaires.

    Ce projet est un outil exploratoire pour l’analyse de grandes quantités de conversations textuelles.


---

Si tu veux, je peux te générer **une version encore plus visuelle du README** avec **captures d’écran du graphe et badges Python/GitHub** pour que ton projet ait un rendu pro sur GitHub.  

Veux‑tu que je fasse ça ?

