from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, template_folder="app/blog/templates")
    app.config.from_object('config.Config')
    
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager = LoginManager()
    login_manager.init_app(app)

    

    # Register Blueprints
    from .auth import auth as auth_blueprint
    from .blog import blog as blog_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(blog_blueprint)

    # Import models after db initialization
    from .models import User

    return app
