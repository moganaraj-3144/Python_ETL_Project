import pandas as pd

def transform(df: pd.DataFrame) -> pd.DataFrame:

    # Convert all columns to lowercase
    df.columns = [col.strip().lower() for col in df.columns]

    # Drop duplicate records
    df = df.drop_duplicates()

    # List of numeric columns
    numeric_cols = ['customer_key', 'customer_id', 'product_key', 'product_id',
                    'cost', 'sales_amount', 'quantity', 'price'] 

    for col in numeric_cols:
        if col in df.columns:
            # Convert everything to string first, strip spaces
            df[col] = df[col].astype(str).str.strip()

            # Replace strings like 'None', '', 'nan' with pd.NA
            df[col] = df[col].replace({'none': pd.NA, '': pd.NA, 'nan': pd.NA})

            # Convert to numeric safely
            df[col] = pd.to_numeric(df[col], errors='coerce')

            # Fill NaN with 0 and convert to int
            df[col] = df[col].fillna(0).astype(int)

    return df
