from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv('MYSQL_USER', 'flaskuser')
password = os.getenv('MYSQL_PASSWORD', 'flask_pass')
host = os.getenv('MYSQL_HOST', 'localhost')
database = os.getenv('MYSQL_DB', 'mendotour')

DATABASE_CONNECTION_URI = f"mysql+pymysql://{user}:{password}@{host}/{database}"
