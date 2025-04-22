# Utiliser une image de base Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier de dépendances (requirements.txt)
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code du bot dans le conteneur
COPY . .

# Définir la commande par défaut pour exécuter le bot
CMD ["python", "bot.py"]
