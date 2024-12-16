from flask import Flask
from api.routes import api_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Подключение Blueprint для API
app.register_blueprint(api_bp)

if __name__ == "__main__":
    app.run(debug=True)
