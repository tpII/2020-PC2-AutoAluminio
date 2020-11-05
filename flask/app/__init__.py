from os import environ
from flask import Flask
from config.config import config
from .db import set_db
from config.routes import set_routes


def create_app(environment="development"):
    # Configuración inicial de la app
    app = Flask(__name__)

    # Carga de la configuración
    env = environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])

    # Establece la db que posee la app
    set_db(app)

    # Establece las rutas que posee la app
    set_routes(app)
 
    # Retornar la instancia de app configurada
    return app
