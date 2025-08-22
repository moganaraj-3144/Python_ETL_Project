import os

POSTGRES = {
    'dev' : {
        'USER':os.environ.get('PG_USER'),
        'PASSWORD':os.environ.get('PG_PASS'),
        'DATABASE':os.environ.get('PG_DB'),
        'HOSTNAME':os.environ.get('PG_HOST'),
        'PORT':os.environ.get('PG_PORT')
    }
}


# Folder containing CSV files
CSV_FOLDER = os.getenv("CSV_FOLDER", "data")