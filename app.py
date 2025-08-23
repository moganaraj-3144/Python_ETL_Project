from extract import read_file_list, extract_files, read_csv_files
from transform import transform
from load import load
import os

def run_etl():
    """Extract the files from file path"""
    file_list = read_file_list("files.txt")

    csv_files = extract_files(file_list)
    if not csv_files:
        print("No CSV files found to process.")
        return
    

    for i in csv_files:
        table_name = os.path.splitext(os.path.basename(i))[0].lower() #csv filename is the table name

        try:
            df = read_csv_files(i)
            print(f'Extracted {len(df)} rows from {i}')

            df = transform(df)
            print(f'Transformed {i}, {len(df)} records')

            load(df, table_name)
            print(f'Successfully loaded {i} into {table_name}')

        except Exception as e:
            print(f'Exception is : {e}')


if __name__ == "__main__":
    run_etl()
