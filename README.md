# 📷 Détection d'Objets Ultra-Légère (Python + TensorFlow.js)

> **Projet de Vision par Ordinateur sans installation complexe.** > *Développé au sein de l'ESP LABORATORY / IUT Sorbonne Nord.*

Ce projet propose une solution de reconnaissance d'objets en temps réel via webcam, conçue pour être **immédiatement utilisable** sans infrastructure lourde ni bibliothèques externes Python.

## 🌟 Points Forts

* **Zéro Dépendance Python** : Fonctionne uniquement avec la bibliothèque standard (`http.server`). Pas de `pip install` nécessaire.
* **Architecture Hybride** : Un serveur local Python ultra-léger propulse une intelligence artificielle exécutée directement dans le navigateur via **TensorFlow.js**.
* **Confidentialité** : Le flux vidéo est analysé localement dans votre navigateur ; aucune image n'est envoyée sur un serveur distant.
* **Performance** : Utilisation du modèle pré-entraîné **COCO-SSD**, capable de reconnaître 90 types d'objets courants avec une latence faible.

## 🚀 Démarrage Rapide

### Prérequis
* Un ordinateur avec une webcam.
* Python installé (n'importe quelle version récente).
* Un navigateur web moderne (Chrome, Firefox, Edge).

### Installation et Lancement
Ce projet est conçu pour être lancé instantanément :

1.  **Cloner ou télécharger** ce dossier.
2.  **Lancer le script** depuis un terminal :
    ```bash
    python detec_ia.py
    ```
3.  **Accéder à l'interface** :
    Ouvrez votre navigateur et allez à l'adresse : `http://localhost:8000`.
4.  **Autoriser la caméra** lorsque le navigateur le demande pour démarrer la détection.

## 🛠️ Comment ça marche ?

Le projet repose sur une approche minimaliste pour faciliter l'apprentissage et le déploiement en milieu associatif ou pédagogique.

1.  **Serveur (Python)** : Le script `detec_ia.py` crée un serveur HTTP simple sur le port **8000** qui sert une page HTML dynamique.
2.  **Client (HTML/JS)** : La page charge **TensorFlow.js** et le modèle **COCO-SSD** via un CDN (Content Delivery Network).
3.  **Inférence (IA)** : Le modèle analyse le flux vidéo image par image directement dans le navigateur et dessine des rectangles (Bounding Boxes) autour des objets détectés avec un score de confiance supérieur à 50%.

## 📦 Objets Détectables

Le modèle est capable d'identifier **90 classes d'objets**, incluant:
* **Personnes & Accessoires** : Personne, sac à dos, parapluie, cravate...
* **Véhicules** : Voiture, vélo, bus, avion, camion...
* **Animaux** : Chat, chien, oiseau, cheval...
* **Objets du quotidien** : Bouteille, téléphone, ordinateur, livre, chaise...

## 👤 Auteur et Contexte

* [cite_start]**Auteur** : Sean VAN NGOC[cite: 4].
* [cite_start]**Contexte** : Projet réalisé entre Mars et Mai 2025 à l'Université Sorbonne Paris Nord (IUT Villetaneuse)[cite: 1, 5].
* [cite_start]**Laboratoire** : IUTVLAB / Association ESP LABORATORY[cite: 9, 10].

---
[cite_start]*Ce projet est une base pédagogique idéale pour illustrer le fonctionnement d'un pipeline IA léger et l'interaction client-serveur.* [cite: 76]
