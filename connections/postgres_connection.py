import psycopg2
from configparser import ConfigParser

def connect_to_postgres():
    # Read the database connection parameters from the database.ini file
    config = ConfigParser()
    config.read('database.ini')

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host=config.get('postgresql', 'host', fallback='localhost'),
        database=config.get('postgresql', 'dbname', fallback='postgres'),
        user=config.get('postgresql', 'user', fallback='postgres'),
        password=config.get('postgresql', 'password', fallback='Bolochoww-44'),
        port=config.get('postgresql', 'port', fallback='5432')
    )

    return conn