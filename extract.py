import os
from config import CSV_FOLDER
import pandas as pd

def read_file_list(file_path="files.txt"):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'{file_path} is not found')
    
    with open(file_path, 'r') as f:
        files = [line.strip() for line in f if line.strip()]

    return files


def extract_files(files):
    files_to_process = []
    for f in files:
        filepath = os.path.join(CSV_FOLDER, f)
        if os.path.exists(filepath):
            files_to_process.append(filepath)
        else:
            print(f"File not found: {f}")

    return files_to_process

def read_csv_files(filename):
    df = pd.read_csv(filename)
    
    return df
