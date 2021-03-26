from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)
    load_dotenv()
    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)

    from commands import db_commands
    app.register_blueprint(db_commands)

    if __name__ == "__main__":
	    app.run(debug=True)
    
    return app

