# Étape 1 : Utiliser une image officielle Python comme image de base
FROM python:3.9-slim

# Étape 2 : Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Étape 3 : Copier le fichier de dépendances dans le conteneur
COPY requirements.txt requirements.txt

# Étape 4 : Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Étape 5 : Copier tout le contenu du projet dans le conteneur
COPY . .

# Étape 6 : Exposer le port utilisé par Flask
EXPOSE 5000

# Étape 7 : Commande pour démarrer l'application
CMD ["python", "app/api.py"]
 
