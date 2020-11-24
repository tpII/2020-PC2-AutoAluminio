from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder

db = SQLAlchemy() # Se crea un objeto de tipo SQLAlchemy
migrate = Migrate()  # Se crea un objeto de tipo Migrate
seeder = FlaskSeeder()

def set_db(app):

    # Configura la base de datos
    db.init_app(app)
    migrate.init_app(app, db)  # Se inicializa el objeto migrate  
    seeder.init_app(app, db)
    with app.app_context():  # Crea un contexto de aplicación
        db.create_all() # Crea las tablas de la base de datos