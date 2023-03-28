from dotenv import load_dotenv
from os import environ

load_dotenv()

HOST = environ.get("HOST", None)
DBNAME = environ.get("DBNAME", None)
USER = environ.get("USER", None)
PASSWORD = environ.get("PASSWORD", None)
PORT = environ.get("PORT", None)
