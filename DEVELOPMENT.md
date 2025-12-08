# Development Workflow

There are two main ways to develop this application: **Local Native** (recommended for speed) and **Docker** (recommended for verification).

## 1. Local Native (Fastest Feedback Loop)
Run the backend and frontend directly on your machine. This provides the fastest hotswapping and debugging experience.

### Backend
1. Open a terminal in the `backend` directory.
2. Activate the virtual environment:
   ```powershell
   venv\Scripts\activate
   ```
3. Run Flask in debug mode (enables hot-reloading):
   ```powershell
   python -m flask --app main run --debug --port 5000
   ```
   *API will be available at http://localhost:5000*

### Frontend
1. Open a terminal in the `frontend` directory.
2. Install dependencies (first time only):
   ```powershell
   npm install
   ```
3. Start the dev server:
   ```powershell
   npm run dev
   ```
   *App will be available at http://localhost:3000* (or the port shown in terminal).

---

## 2. Docker with Hotswap
You can also develop within Docker containers while keeping hot-reloading enabled by using **Bind Mounts**.

### Setup
We have configured `docker-compose.yaml` to mount your local source code into the running containers.
- **Backend:** `./backend` maps to `/project`. Changes to python files inside `backend` will trigger a Flask reload.
- **Frontend:** `./frontend` maps to `/frontend`. Changes to sync files will trigger Vite HMR.

### Running
1. Start the services:
   ```powershell
   docker compose up --build
   ```
2. Access the app at http://localhost:3000.

### Note on Database
The SQLite database `backend/sqlite_main.db` is mounted to persist data. You can access this file locally to inspect data.
