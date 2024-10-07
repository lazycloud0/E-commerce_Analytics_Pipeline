import pandas as pd
from sqlalchemy import create_engine

def load_data(df, table_name, db_uri):
    """Load data into the data warehouse."""
    engine = create_engine(db_uri)
    df.to_sql(table_name, engine, if_exists='replace', index=False)