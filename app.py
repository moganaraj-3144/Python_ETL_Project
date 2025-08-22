from extract import read_file_list, extract_files, read_csv_files
from transform import transform
import os

def run_etl():
    """Extract the files from file path"""
    file_list = read_file_list("files.txt")

    csv_files = extract_files("files")

    for i in csv_files:
        df = read_csv_files(i)

        table_name = os.path.splitext(os.path.basename(i))[0].lower() #csv filename is the table name

        df = transform(df)

    return 

if __name__ == "__main__":
    run_etl()
