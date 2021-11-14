from flask import Flask, jsonify, request
import re
from app.models.user_model import User
from app.exceptions.users_exceptions import IdIsNotInstanceOfTypeDigitException, NonexistentUserException


"""
    Function that manages a collection of routes, that
    executes methods to CREATE, RETURN, UPDATE and DELETE
    users from the database.
"""
def home_view(app: Flask):
    
    """
        Application route that gets a list of all users
        from database, using a GET Http method in the /users
        link.
    """
    @app.route('/users', methods=['GET'])
    def get_users():

        """
            Executing the User class method get_all to get 
            a list of all users from the database, and returning
            into a variable.
        """
        data: list = User.get_all()

        """
            Using a statement to check if the data list is empty.
            If the condition is True, this converts the data list
            to a json object and returns it with the Http code
            200.  
            If the condition is False, this return a message with
            the Http code 200.
        """
        if data != []:
            return jsonify(data), 200
        else:
            return 'Empty', 404

    """
        Application route that creates a user and save it into
        the database, using a POST Http method in the /users
        link.
    """
    @app.route('/users', methods=['POST'])
    def create_user():

        """
            Using the try/except statement to catch and treat
            the exceptions.
        """
        try:

            """
                Using the get_json method from the request
                library, to get the body of the requisition
                and save it into a variable.
                This method allows you to send data to the
                server, using a JSON file.
            """
            data = request.get_json()

            """
                Creating a User object with the data provided
                in the body of the requisition.
            """
            user: User = User(**data)

            """
                Using the User class method save, to save the
                user into the database.
            """
            User.save(user)

            """
                Returning the user data in a dictionary format
                with the Http code 201.
            """
            return user.__dict__, 201
        
        except TypeError as e:

            """
                Formatting the error message using a regex that
                substitutes the parentheses, commas and double
                quotes by an empty value.
                The e.args function returns a tuple with the
                error message, but the regex function only 
                accepts string, so we must convert it.
            """
            e: str = re.sub('[(",)]', '', str(e.args))

            """
                Returning the formatted message with the Http
                code 400.
            """
            return f'Message: {e}', 400

    """
        Application route that deletes a user from the database,
        using a POST Http method in the /users/ link passing as 
        parameter the user id.
    """
    @app.route('/users/<id>', methods=['DELETE'])
    def delete_user(id: str):

        try:
            """
                Using the User class method delete to delete the
                user in the database, and return an empty message
                with the Http status code 204.
            """
            User.delete(id)
            return '', 204

        except IdIsNotInstanceOfTypeDigitException as e:
            """
                Returning the error message defined in the
                exception raise.
            """
            return e.get_message(), 400

        except NonexistentUserException as e:
            return e.get_message(), 404

    """
        Application route that updates a user from the database,
        using a PATCH Http method in the /users/ link passing as 
        parameter the user id.
    """
    @app.route('/users/<id>', methods=['PATCH'])
    def update_user(id: str):
        pass
