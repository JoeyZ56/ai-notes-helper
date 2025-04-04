# Docs

## Setting up Backend:

### Create a Virtual Environment

1.  Create venv folder:

        python3.12 -m venv venv
        source venv/bin/activate

2.  Install FastAPI + Uvicorn

        pip install fastapi uvicorn

3.  Run the Backend

        uvicorn app.main:app --reload

- Check in your browser: http://localhost:8000

- URL link will show: {"message":"Hello from FastAPI"}

---
