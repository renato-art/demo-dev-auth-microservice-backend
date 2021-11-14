from flask import Flask
from app.views.home_view import home_view


"""
    Function that initiates the project Views
"""
def init_app(app: Flask):

    """
        Loads the home_view that has the controll of the
        project routes.
    """
    home_view(app)

    return app
    