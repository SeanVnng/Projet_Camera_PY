# Projet_Camera_PY - Détection d'Objets IA

Projet_Camera_PY est une application de vision par ordinateur minimaliste capable de détecter des objets en temps réel via une webcam. Elle repose sur un serveur local Python et l'exécution d'une IA directement dans le navigateur.

## 🚀 Fonctionnalités

* **Détection Intelligente** :
    * [cite_start]Reconnaissance en temps réel via le modèle **COCO-SSD**[cite: 22, 26].
    * [cite_start]Identification de **90 objets** (personnes, véhicules, animaux...)[cite: 26, 73].
    * [cite_start]Affichage du score de confiance et cadres de détection[cite: 30, 31].
* **Zéro Installation** :
    * [cite_start]**Aucune bibliothèque externe** requise (pas de pip install)[cite: 17, 25].
    * [cite_start]Utilisation exclusive de la librairie standard Python[cite: 19, 25].
* **Architecture Légère** :
    * [cite_start]Serveur HTTP local rapide (`http.server`)[cite: 20, 45].
    * [cite_start]Inférence IA côté client (TensorFlow.js)[cite: 72].
    * [cite_start]Fonctionne hors-ligne une fois chargé[cite: 36].

## 📂 Structure du Projet

Le projet tient en un seul script principal pour une simplicité maximale :

```text
Projet_Camera_PY/
├── detec_ia.py          # Script principal (Serveur + Interface)
├── README.md            # Documentation
└── Rapport...pdf        # Documentation technique détaillée
