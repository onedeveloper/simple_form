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
    routes/     Placeholder API routes
    schemas/    Pydantic models
  main.py       Application entrypoint
  requirements.txt

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
parameters are read from environment variables:

- `MONGO_URI` – MongoDB connection string (default:
  `mongodb://localhost:27017`)
- `MONGO_DB_NAME` – database name (default: `simple_form`)

## Running the Backend

1. Create a virtual environment and install dependencies:

   ```bash
   cd backend
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

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

## Notes

This project currently contains only placeholder routes and components.
Additional logic for form creation, rendering and submission should be
implemented in the respective backend and frontend folders.

