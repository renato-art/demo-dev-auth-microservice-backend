Feature: Get users from database
    In order to show the users from the Postgres database,
    we will use a User object and a Flask application route
    to make a connection with the database and get all data
    from the users table.

    Scenario: Getting all users
        When I submit a get request in the main route 
        Then show a list with all users of the database
