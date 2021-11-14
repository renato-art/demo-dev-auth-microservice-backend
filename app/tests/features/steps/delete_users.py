from behave import *
from psycopg2 import sql
from app.models.user_model import User
from app.tests.features.environment import client, db_connection, db_commiting_and_closing

@when(u'I submit a delete request with an user id')
def step_impl(context):
    
    conn, cur = db_connection()

    cur.execute("""
        INSERT INTO users(name, email, password) 
        VALUES ('psycopg2test', 'test@mail.com', '12345678')
    """)

    cur.execute("""
        SELECT name, email, password FROM users WHERE name = 'psycopg2test'
    """)

    user = list(cur.fetchall())

    db_commiting_and_closing(conn, cur)

    user_model_to_compare: list = [("psycopg2test", "test@mail.com", "12345678")]

    assert user == user_model_to_compare
    

@then(u'delete the user')
def step_impl(context):
    conn, cur = db_connection()

    cur.execute("""
        SELECT id FROM users WHERE name = 'psycopg2test'
    """)

    user_id = cur.fetchall()

    client(context).delete(f'/users/{user_id[0][0]}')

    cur.execute("""
        SELECT id FROM users WHERE name = 'psycopg2test'
    """)

    data = cur.fetchall()

    db_commiting_and_closing(conn, cur)

    assert data == []
