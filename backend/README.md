# Backend du site de gestion de chantier

API REST développée avec [FastAPI](https://fastapi.tiangolo.com/) et exécutée avec Python 3.13 ou supérieur.

## Installation (Windows / PowerShell)

Depuis le dossier `backend` :

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .
```

Si PowerShell empêche l'activation de l'environnement virtuel, utilisez directement son interpréteur :

```powershell
.\.venv\Scripts\python.exe -m pip install -e .
```

## Démarrer le serveur

Dans le dossier `backend`, avec l'environnement virtuel activé :

```powershell
fastapi dev main.py
```

Le serveur de développement écoute sur [http://localhost:8000](http://localhost:8000). Pour lancer FastAPI sans activer l'environnement virtuel :

```powershell
.\.venv\Scripts\fastapi.exe dev main.py
```

## Démarrer avec Docker Compose

Depuis le dossier `backend` :

```powershell
docker compose up --build -d
```

Cette commande démarre PostgreSQL, l'API et le frontend. Pour démarrer l'API et le frontend ainsi que les dépendances nécessaires :

```powershell
docker compose up --build -d backend frontend
```

Afficher les logs ou arrêter les conteneurs :

```powershell
docker compose logs -f
docker compose down
```

Le frontend est accessible au port défini par `FRONTEND_PORT` dans `.env` (3001 dans la configuration locale actuelle). L'API écoute sur le port défini par `BACKEND_PORT` (8000 par défaut).

La documentation interactive des routes est disponible sur [http://localhost:8000/docs](http://localhost:8000/docs), et le schéma OpenAPI sur [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json).

## Routes disponibles

| Méthode | Route | Description |
| --- | --- | --- |
| `GET` | `/health-check` | Vérifie que l'API répond. Retourne `{"status":"healthy"}`. |
| `GET` | `/api/data` | Retourne un exemple de données : un message et une liste d'entiers. |

## Configuration CORS

En développement, l'API autorise les requêtes cross-origin depuis `http://localhost:3000`, l'adresse locale du frontend. Si le frontend utilise une autre adresse, modifiez `allow_origins` dans `main.py`.

## Dépendances

Les dépendances Python sont déclarées dans `pyproject.toml`. La dépendance directe du projet est `fastapi[standard]`.
