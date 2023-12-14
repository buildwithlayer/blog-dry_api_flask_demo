# Local Imports
from config import create_app
from routes import farmers_bp

app = create_app()
app.register_blueprint(farmers_bp, url_prefix="/farmers")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
