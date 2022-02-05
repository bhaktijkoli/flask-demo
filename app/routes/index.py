from app import app


@app.route("/", methods=["GET"])
def get():
    return "Welcome to API"
