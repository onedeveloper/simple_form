# Simple Form Project

This repository contains a minimal scaffolding for a dynamic form system
with a FastAPI backend and a React (TypeScript) frontend. The project is
split into two parts:

- **Form Builder** – allows creating and versioning forms.
- **Form Runner** – renders forms for users to fill out.

## Project Structure

```
backend/        FastAPI application
  app/
    db/         MongoDB connection utilities
    routes/     API routes
    schemas/    Pydantic models
  tests/        Test suite skeleton
  scripts/      Utility scripts
  main.py       Application entrypoint
  
frontend/       React application powered by Vite
  src/          React source files
    App.tsx
    main.tsx
  index.html    Entry HTML file
  package.json  Frontend dependencies
  tsconfig*.json TypeScript configuration
```

## MongoDB Connection

The backend uses **Motor** for asynchronous MongoDB access. Connection
details are provided via the `MONGO_USER`, `MONGO_PASSWORD`, `MONGO_HOST`,
`MONGO_DBNAME` and `MONGO_APPNAME` environment variables.

## Running the Backend

1. Create a local Python virtual environment and install dependencies:

   ```bash
   cd backend
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

   Create a `.env` file based on `.env.example` and provide your MongoDB
   connection details.

2. Start the FastAPI app:

   ```bash
   uvicorn main:app --reload
   ```

## Running the Frontend

1. Install Node dependencies:

   ```bash
   cd frontend
   npm install
   ```

2. Start the development server:

   ```bash
   npm run dev
   ```

The frontend will be available at `http://localhost:3000`.

## Deployment

### Railway (Backend)

1. Create a new project on [Railway](https://railway.app/).
2. Point it at this repository and set the MongoDB connection variables
   (`MONGO_USER`, `MONGO_PASSWORD`, `MONGO_HOST`, `MONGO_DBNAME`,
   `MONGO_APPNAME`) in the environment settings.
3. Railway will automatically install dependencies from `requirements.txt`
   and run `uvicorn main:app`.

### Vercel (Frontend)

1. Import the `frontend/` directory as a new Vercel project.
2. Use the default **Vite** build settings (`npm run build`).
3. Set the `VITE_BACKEND_URL` environment variable to the base URL of your
   deployed backend (for local development you can use `http://localhost:8000`).
4. Deploy and your React app will be available on Vercel.

## Notes

This project originally contained only placeholder routes and components.
The frontend now includes a very small **Form Builder** implementation that
allows you to enter a form name and dynamically add questions. The builder
submits the form definition to the backend via the `/forms` endpoint.

