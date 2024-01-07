import os
import psycopg2

user = os.getenv('POSTGRES_USER')
password = os.getenv('POSTGRES_PASSWORD')
database = os.getenv('POSTGRES_DB')
connection = psycopg2.connect(user=user, password=password, host='localhost', database=database)