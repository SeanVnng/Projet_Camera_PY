# Projet_Camera_PY - Détection d'Objets IA

Projet_Camera_PY est une application de vision par ordinateur minimaliste capable de détecter des objets en temps réel via une webcam. Elle repose sur un serveur local Python et l'exécution d'une IA directement dans le navigateur.

## 🚀 Fonctionnalités

* **Détection Intelligente** :
    * Reconnaissance en temps réel via le modèle **COCO-SSD**.
    * Identification de **90 objets** (personnes, véhicules, animaux...).
    * Affichage du score de confiance et cadres de détection.
* **Zéro Installation** :
    * **Aucune bibliothèque externe** requise (pas de pip install).
    * Utilisation exclusive de la librairie standard Python.
* **Architecture Légère** :
    * Serveur HTTP local rapide (`http.server`).
    * Inférence IA côté client (TensorFlow.js).
    * Fonctionne hors-ligne une fois chargé.

## 📂 Structure du Projet

Le projet tient en un seul script principal pour une simplicité maximale :

```text
Projet_Camera_PY/
├── detec_ia.py          # Script principal (Serveur + Interface)
├── README.md            # Documentation
└── Rapport...pdf        # Documentation technique détaillée
