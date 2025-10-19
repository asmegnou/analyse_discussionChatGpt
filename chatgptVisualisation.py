import json
import pandas as pd
from pyvis.network import Network
from sentence_transformers import SentenceTransformer, util
import torch
from textwrap import shorten

# === 1. Charger les données exportées ===
with open("conversations.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# === 2. Extraire les titres et messages ===
conversations = []
for conv in data:
    title = conv.get("title", "Sans titre")
    messages_list = []

    for node in conv.get("mapping", {}).values():
        message = node.get("message")
        if message and "content" in message and "parts" in message["content"]:
            parts = message["content"]["parts"]
            if parts and isinstance(parts[0], str):
                messages_list.append(parts[0])

    messages = " ".join(messages_list).strip()
    if messages:  # ignorer les conversations vides
        conversations.append({"title": title, "messages": messages})

df = pd.DataFrame(conversations)
print(f"📊 {len(df)} conversations chargées.")

# (Optionnel) : limiter à 200 conversations pour la performance
df = df.head(500)

# === 3. Calcul des embeddings sémantiques avec PyTorch ===
# === Détection automatique du bon device ===
if torch.backends.mps.is_available():
    device = "mps"   # GPU Apple Silicon
    print("Utilisation du GPU Apple (MPS).")
elif torch.cuda.is_available():
    device = "cuda"  # GPU NVIDIA (si jamais)
    print("Utilisation du GPU NVIDIA (CUDA).")
else:
    device = "cpu"   # CPU classique
    print("Utilisation du CPU (pas de GPU disponible).")

model = SentenceTransformer("all-MiniLM-L6-v2", device=device)

# Encoder les textes
embeddings = model.encode(df["messages"].tolist(), convert_to_tensor=True, show_progress_bar=True)

# === 4. Calculer la similarité cosinus ===
similarity_matrix = util.cos_sim(embeddings, embeddings)

# === 5. Construire le graphe PyVis ===
net = Network(height="750px", width="100%", bgcolor="#ffffff", font_color="black")
net.force_atlas_2based()  # meilleure répartition des nœuds

# Ajouter les nœuds
for i, row in df.iterrows():
    label = shorten(row["title"], width=40, placeholder="…")
    tooltip = shorten(row["messages"], width=300, placeholder="…")
    net.add_node(i, label=label, title=tooltip)

# === 6. Ajouter des arêtes selon la similarité ===
threshold = 0.5  # augmente (0.6-0.7) pour un graphe plus léger
print(f"🔗 Création des liens (seuil de similarité = {threshold})...")

for i in range(len(df)):
    for j in range(i + 1, len(df)):
        sim = similarity_matrix[i][j].item()
        if sim > threshold:
            net.add_edge(i, j, value=sim)

# === 7. Générer le graphe interactif ===
net.write_html("graphe_conversations_semantique.html", notebook=False)
print("Fichier HTML généré : ouvre 'graphe_conversations_semantique.html' manuellement dans ton navigateur.")
