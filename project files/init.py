from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(_name_)
    
    # Configuration
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['UPLOAD_FOLDER'] = 'uploads'
    
    # Enable CORS for cross-origin access
    CORS(app)

    # Register blueprints or routes
    from .routes import main
    app.register_blueprint(main)

    return app