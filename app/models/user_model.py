from app.exceptions.users_exceptions import IdIsNotInstanceOfTypeDigitException, NonexistentUserException
import psycopg2
from psycopg2 import sql
from environs import Env

"""
    Instantiating the Env object to read the environment 
    content.
"""
env: Env = Env()
env.read_env()

"""
    Creating the variables to store the environment content.
"""
db_host: str = env("DB_HOST")
db_name: str = env("DB_NAME")
db_user: str = env("DB_USER")
db_password: str = env("DB_PASSWORD")


class User():

    """
        Creating a constant to store the columns names from 
        users tables.
    """
    FIELDNAMES: list = ["id", "name", "email", "password"]

    """
        Method that instantiates the User object variables.
    """
    def __init__(self, name: str, email: str, password: str):
        self.name: str = name
        self.email: str = email
        self.password: str = password

    """
        Class method that returns a list with the users 
        table and your values.
    """
    @staticmethod
    def get_all() -> list:
        
        """
            Getting the database variables from db_connection
            class method.
            The conn variable is responsible to connect to the
            Postgres database.
            The cur variable is responsible to create a cursor
            to execute queries inside the database.
        """
        conn, cur = User.db_connection()

        """
            Executing a query that select all columns and values
            from users table.
        """
        cur.execute("""
            SELECT * FROM users
        """)

        """
            Getting the data collected in the past query and assigning
            to a variable.
        """
        data = cur.fetchall()

        """
            Creating a dictionaries list with the columns names in 
            the keys, the query values in the values and returning 
            to a variable.
        """
        processed_data: list = [dict(zip(User.FIELDNAMES, row)) for row in data]

        """
            Using the db_commiting_and_closing class method to commit 
            the database modifications, and to close the cursor and 
            database connection.
        """
        User.db_commiting_and_closing(conn, cur)

        return processed_data

    """
        Class method responsible to save the user object into the 
        database.
    """
    @staticmethod
    def save(user):

        conn, cur = User.db_connection()

        """
            Getting the user values, converting into a list and 
            returning to a variable.
        """
        new_user: list  = list(user.__dict__.values())

        """
            Creating a query to insert the user values into the 
            database.
            The method 'sql.SQL()' is used to prevent malicious
            strings, that performs forbidden queries in the
            database.
            The join method of the sql library, converts a list
            to a string, using a character as join parameter.
        """
        query = sql.SQL(
            """
                INSERT INTO users(name, email, password) VALUES ({user_values})
            """
        ).format(user_values = sql.SQL(',').join(sql.Literal(value) for value in new_user))

        """
            Function that executes the query last created.
        """
        cur.execute(query)

        User.db_commiting_and_closing(conn, cur)

    """
        Class method responsible to delete an user from the database,
        using an id as query parameter. 
    """
    @staticmethod
    def delete(id: str):

        """
            Checking if the id variable is possible to convert into int.
            If the condition is not valid, the function raises an
            IdIsNotInstanceOfTypeDigitException error with a message.
        """
        try:
            int(id)
        except ValueError:
            raise IdIsNotInstanceOfTypeDigitException(f"The id variable is not a digit.")

        """
            Creating a variable that indicates if the user exists
            inside the database.
        """
        user_exists = False

        conn, cur = User.db_connection()

        cur.execute("""
        SELECT * FROM users
        """)

        data = cur.fetchall()

        processed_data = [dict(zip(User.FIELDNAMES, row)) for row in data]

        """
            Executing a for loop to read all users collected in the
            last query.
        """
        for item in processed_data:
            """
                Testing if the id provided in the method, is equal
                to the id of a user present in the list.
                The conversion of the variable to an Int instance
                is necessary, because the id returned from the
                database is an Integer.
            """
            if item["id"] == int(id):
                """
                    Turning the user_exists variable to True if a 
                    user with the provided id exists.
                """
                user_exists = True

        """
            Checking if the user_exists variable is equal to True.
            If the condition is valid, the function raises an
            NonexistentUserException error with a message.
        """
        if user_exists != True:
            raise NonexistentUserException("User doesn't exists")

        """
            Creating a query to delete the user from database where
            the id is equal to the id provided in the method.
        """
        query = sql.SQL(
            """
                DELETE FROM users WHERE id = {user_id}
            """
        ).format(user_id = sql.Literal(id))

        cur.execute(query)

        User.db_commiting_and_closing(conn, cur)

    @staticmethod
    def db_connection():

        """
            Establishing a connection to a Postgres database,
            using the environments variables defined before.
        """
        conn = psycopg2.connect(host=db_host, database=db_name,
                              user=db_user, password=db_password)

        """
            Creating a cursor instance to make the queries inside
            the database.
        """
        cur = conn.cursor()

        return conn, cur

    @staticmethod
    def db_commiting_and_closing(conn, cur):

        """
            Function that commits the changes made inside the database.
        """
        conn.commit()

        """
            Function that closes the cursor instance.
        """
        cur.close()

        """
            Function that closes the connection with the database.
        """
        conn.close()
