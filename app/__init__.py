from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
# from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "SQLALCHEMY_DATABASE_URI")

    db.init_app(app)
    migrate.init_app(app, db)

    # Import models here for Alembic setup
    from app.models.Event import Event
    from app.models.Pet import Pet

    # Register Blueprints here
    from app.routes.pet_routes import pets_bp
    app.register_blueprint(pets_bp)
    from app.routes.event_routes import events_bp
    app.register_blueprint(events_bp)

    # pets_bp.register_blueprint(events_bp)
    # app.register_blueprint(pets_bp)
    

    # CORS(app)
    return app
