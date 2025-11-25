#  Étape 1 : Choisir l'image de base 
    FROM python:3.11-bullseye

    #  Étape 2 : Définir le répertoire de travail dans le conteneur 
    WORKDIR /app
    
    #  Étape 3 : Copier les fichiers nécessaires 
    COPY requirements.txt .
    
    #  Étape 4 : Installer les dépendances 
    RUN pip install --no-cache-dir -r requirements.txt
    
    #  Étape 5 : Copier tout le projet 
    COPY . .
    
    #  Étape 6 : Exposer le port Flask 
    EXPOSE 5000
    
    #  Étape 7 : Commande de lancement 
    CMD ["python", "run.py"]
    