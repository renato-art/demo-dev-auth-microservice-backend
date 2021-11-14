from behave import *
from psycopg2 import connect
from app.models.user_model import User
from app.tests.features.environment import client, db_connection, db_commiting_and_closing

users_list = []

@when(u'I submit a get request in the main route')
def step_impl(context):
    global users_list
    users_list = client(context).get('/users')

@then('show a list with all users of the database')
def step_impl(context):
    conn, cur = db_connection()

    cur.execute("""
        SELECT * FROM users
    """)
    
    data = cur.fetchall()

    FIELDNAMES = ["id", "name", "email", "password"]
    users_list_to_compare = [dict(zip(FIELDNAMES, row)) for row in data]

    db_commiting_and_closing(conn, cur)

    assert users_list.get_json() == users_list_to_compare
