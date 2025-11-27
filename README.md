# Projet_Camera_PY - Détection d'Objets IA

Projet_Camera_PY est une application légère de vision par ordinateur capable de détecter et classifier des objets en temps réel via une webcam. Elle repose sur un serveur Python local et l'exécution du modèle IA directement dans le navigateur.

## 🚀 Fonctionnalités

* **Détection Temps Réel** :
    * [cite_start]Reconnaissance via webcam avec cadres de détection[cite: 30].
    * [cite_start]Modèle **COCO-SSD** capable d'identifier 90 objets (personnes, téléphones, bouteilles...)[cite: 26].
    * [cite_start]Affichage du score de confiance pour chaque objet[cite: 31].
* **Zéro Installation** :
    * [cite_start]Aucune bibliothèque externe requise (pas de `pip install`)[cite: 17].
    * [cite_start]Utilise uniquement Python standard (`http.server`)[cite: 25].
* **Architecture Légère** :
    * [cite_start]Serveur HTTP local rapide.
    * [cite_start]Fonctionne hors-ligne une fois chargé[cite: 36].
    * Compatible tout navigateur moderne.

## 📂 Structure du Projet

Le projet est conçu pour être simple et minimaliste :

```text
Projet_Camera_PY/
├── detec_ia.py          # Script principal (Serveur Python + Code HTML/JS)
└── README.md            # Documentation

Réalisé par Seann
