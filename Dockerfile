# Utilisation d'une image Python
FROM python:3.10

# Définition du répertoire de travail
WORKDIR /app

# Copie des fichiers nécessaires
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code source
COPY . .

# Commande par défaut
CMD ["python", "main.py"]