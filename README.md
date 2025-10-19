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
