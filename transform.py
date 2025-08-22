import pandas as pd

def transform(df:pd.dataframe) -> pd.dataframe:
    df = df.head()
    # Convert all columns to lowercase
    df.colummns = [cols.strip.lower() for cols in df.columns]

    # Drop duplicate records
    df = df.drop_duplicates()

    return df