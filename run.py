from app import app
import os

if __name__ == "__main__":

    # RUN APPLICATION
    app.run(host="0.0.0.0", port=os.getenv("FLASK_PORT", 8000), load_dotenv=True)
