import os
from dotenv import load_dotenv
import psycopg2

current_dir = os.path.dirname(__file__)
dotenv_path = os.path.join(current_dir, '..', '.env')
load_dotenv(dotenv_path)

user = os.getenv('POSTGRES_USER')
password = os.getenv('POSTGRES_PASSWORD')
database = os.getenv('POSTGRES_DB')
connection = psycopg2.connect(user=user, password=password, host='localhost', database=database)