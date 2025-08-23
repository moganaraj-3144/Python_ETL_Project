import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="credentials.env")

POSTGRES = {
    'dev' : {
        'USER':os.getenv('PG_USER'),
        'PASSWORD':os.getenv('PG_PASS'),
        'DATABASE':os.getenv('PG_DB'),
        'HOSTNAME':os.getenv('PG_HOST'),
        'PORT':os.getenv('PG_PORT')
    }
}

# Folder containing CSV files
CSV_FOLDER = os.getenv("CSV_FOLDER","/Users/mogana/myProjects/SQL_Data_Warehouse_Project/datasets/csv-files")