from os import environ

class BaseConfig(object):
    """Base configuration."""

    DEBUG = None
    DB_HOST = "bd_name"
    DB_USER = "db_user"
    DB_PASS = "db_pass"
    DB_NAME = "db_name"
    SECRET_KEY = "2082f13cf5b64124a7a37896a1ef2fe3"

    @staticmethod
    def configure(app):
        # Implement this method to do further configuration on your app.
        pass


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    ENV = "development"
    DEBUG = environ.get("DEBUG", True)
    DB_HOST = environ.get("DB_HOST", "localhost")
    DB_USER = environ.get("DB_USER")
    DB_PASS = environ.get("DB_PASS")
    DB_NAME = environ.get("DB_NAME")
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:3306/{DB_NAME}"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(BaseConfig):
    """Testing configuration."""

    ENV = "testing"
    TESTING = True
    DEBUG = environ.get("DEBUG", True)
    DB_HOST = environ.get("DB_HOST", "localhost")
    DB_USER = environ.get("DB_USER")
    DB_PASS = environ.get("DB_PASS")
    DB_NAME = environ.get("DB_NAME")
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:3306/{DB_NAME}"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    """Production configuration."""

    ENV = "production"
    DEBUG = environ.get("DEBUG", False)
    DB_HOST = environ.get("DB_HOST", "")
    DB_USER = environ.get("DB_USER", "")
    DB_PASS = environ.get("DB_PASS", "")
    DB_NAME = environ.get("DB_NAME", "")
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:3306/{DB_NAME}"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = dict(
    development=DevelopmentConfig, testing=TestingConfig, production=ProductionConfig
)
