import pandas as pd
import sqlalchemy
from config import POSTGRES
from urllib.parse import quote_plus

def create_connection(env ='dev'):

    try :
        db_creds = POSTGRES[env]

        # Encode any special characters
        user = quote_plus(db_creds['USER'])
        password = quote_plus(db_creds['PASSWORD'])

        # Create connection to DB
        conn_uri = f"postgresql+psycopg2://{user}:{password}@{db_creds['HOSTNAME']}:{db_creds['PORT']}/{db_creds['DATABASE']}"
       
        db_engine = sqlalchemy.create_engine(conn_uri)
        print(f"Connected to {env} database successfully")
        return db_engine
    
    except Exception as e:
        print(f'Exception is :{e}')


def load(df, table_name, env = 'dev'):

    try:
        db_engine = create_connection(env)
        
        if db_engine is None:
            raise Exception("Database connection failed")
        
        df.to_sql(
                name = table_name,
                con = db_engine,
                if_exists = "append",
                index = False,
                schema = "gold"
            )
        
        db_engine.dispose()
        
        print(f'Loaded {len(df)} records into table:{table_name}')
    
    except Exception as e:
     
        print(f"Exception is:{e}")