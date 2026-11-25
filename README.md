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

