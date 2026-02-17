from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # ==============================
    # Database config
    # ==============================
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://apple@localhost:5432/productdb"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # ==============================
    # Swagger config
    # ==============================
    app.config["SWAGGER"] = {
        "title": "Flask Product API",
        "uiversion": 3,
    }

    db.init_app(app)
    Swagger(app)  # ⭐ enable swagger

    # ==============================
    # Register blueprints
    # ==============================
    from app.routes import product_bp
    app.register_blueprint(product_bp)

    # ==============================
    # Create tables automatically
    # ==============================
    with app.app_context():
        db.create_all()

    return app
