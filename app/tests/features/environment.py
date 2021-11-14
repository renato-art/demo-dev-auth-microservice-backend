from behave import fixture, use_fixture
import psycopg2
from app import create_app
from environs import Env

env = Env()
env.read_env()

db_host = env("DB_HOST")
db_name = env("DB_NAME")
db_user = env("DB_USER")
db_password = env("DB_PASSWORD")

@fixture
def client(context, *args, **kwargs):
    create_app().testing = True
    context.client = create_app().test_client()

    return context.client


def before_feature(context, feature):
    use_fixture(client, context)


def db_connection():
    conn = psycopg2.connect(host=db_host, database=db_name,
                              user=db_user, password=db_password)

    cur = conn.cursor()

    return conn, cur


def db_commiting_and_closing(conn, cur):
    conn.commit()

    cur.close()

    conn.close()
