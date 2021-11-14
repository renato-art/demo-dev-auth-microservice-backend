from flask import Flask
from app import views
from environs import Env

"""
    Function that creates and returns a Flask instance
"""
def create_app():

    """
        This loads and reads the environment variables in the
        .env file.
    """
    env = Env()
    env.read_env()
    
    """
        Creating a Flask instance.
    """    
    app = Flask(__name__)

    """
        Initializing the project routes present in the Views 
        library.
    """
    views.init_app(app)

    return app
    