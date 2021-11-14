Feature: Deleting a user from database
    In order to test the delete function from User model,
    we will create a test user, and get your id to make
    a query in the database to delete the user created
    in this task.

    Scenario: Creating and deleting the user psycopg2test
        When I submit a delete request with an user id
        Then delete the user
        