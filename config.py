# Snowflake= { 'account' : 'elaopul-va59850',
#                     'user': 'Nandinireddy2002',
#                     'password' : 'Nandini$123',
#                     'database' : 'STAFFMANAGEMENT',
#                     'schema' : 'PUBLIC'
# }

from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SNOWFLAKE_USER = os.getenv('SNOWFLAKE_USER')
    SNOWFLAKE_PASSWORD = os.getenv('SNOWFLAKE_PASSWORD')
    SNOWFLAKE_ACCOUNT = os.getenv('SNOWFLAKE_ACCOUNT')
    SNOWFLAKE_DATABASE = os.getenv('SNOWFLAKE_DATABASE')
    SNOWFLAKE_SCHEMA = os.getenv('SNOWFLAKE_SCHEMA')
    SECRET_KEY = os.urandom(24)

    @staticmethod
    def print_env_variables():
        print("SNOWFLAKE_USER:", Config.SNOWFLAKE_USER)
        print("SNOWFLAKE_PASSWORD:", Config.SNOWFLAKE_PASSWORD)
        print("SNOWFLAKE_ACCOUNT:", Config.SNOWFLAKE_ACCOUNT)
        print("SNOWFLAKE_DATABASE:", Config.SNOWFLAKE_DATABASE)
        print("SNOWFLAKE_SCHEMA:", Config.SNOWFLAKE_SCHEMA)
