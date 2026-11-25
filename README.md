# Projet Teknosure

Application composée d'une API **FastAPI** et d'une interface web **Next.js**.

## Prérequis

- Python 3.13 ou supérieur
- Node.js et npm
- PowerShell (commandes ci-dessous prévues pour Windows)

## Installation et lancement

Lancez chaque partie dans son propre terminal.

### Backend (FastAPI)

Depuis la racine du projet :

```powershell
cd backend
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .
fastapi dev main.py
```

L'API est disponible sur [http://localhost:8000](http://localhost:8000). La documentation interactive se trouve sur [http://localhost:8000/docs](http://localhost:8000/docs).

Si PowerShell bloque l'activation de l'environnement virtuel, vous pouvez appeler directement son exécutable :

```powershell
.\.venv\Scripts\python.exe -m pip install -e .
.\.venv\Scripts\fastapi.exe dev main.py
```

### Frontend (Next.js)

Dans un autre terminal, depuis la racine du projet :

```powershell
cd frontend
npm install
npm run dev
```

L'interface est disponible sur [http://localhost:3000](http://localhost:3000).

## Lancement avec Docker

Le fichier Compose se trouve dans `backend/docker-compose.yml`. Depuis la racine du projet, démarrez la base de données, l'API et le frontend avec :

```powershell
docker compose -f backend/docker-compose.yml up --build -d
```

Pour démarrer uniquement le backend et le frontend (Compose démarre aussi la base nécessaire au backend) :

```powershell
docker compose -f backend/docker-compose.yml up --build -d backend frontend
```

Le frontend utilise le port défini par `FRONTEND_PORT` dans `backend/.env` (3001 dans la configuration locale actuelle). L'API est disponible sur le port défini par `BACKEND_PORT` (8000 par défaut), avec sa documentation sur `/docs`.

Afficher les logs :

```powershell
docker compose -f backend/docker-compose.yml logs -f
```

Arrêter les conteneurs :

```powershell
docker compose -f backend/docker-compose.yml down
```

## Routes de l'API

| Méthode | Route | Réponse |
| --- | --- | --- |
| `GET` | `/health-check` | État de santé de l'API (`{"status":"healthy"}`) |
| `GET` | `/api/data` | Exemple de données renvoyées par le backend |

Le backend autorise les requêtes CORS provenant de `http://localhost:3000` pour le développement local.

## Structure du projet

```text
.
├── backend/       # API FastAPI (main.py, pyproject.toml)
└── frontend/      # Application Next.js
```

