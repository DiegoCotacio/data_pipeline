from connections.postgres_connection import connect_to_postgres
from connections.bigquery_connection import connect_to_bigquery
import psycopg2
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
#from google.cloud import bigquery

def extract_data():
    # Connect to the PostgreSQL database
    conn = connect_to_postgres()

    # Create a cursor object
    cursor = conn.cursor()

    # Execute the SQL query
    cursor.execute("SELECT * FROM mltests")

    # Fetch the results of the query
    results = cursor.fetchall()

    # Close the cursor and the connection
    cursor.close()
    conn.close()

    # Return the results
    return results



def transform_data(data):
    # Fetch data from the mltests table
    #data = extract_data()

    # Convert the fetched data into a pandas DataFrame
    df = pd.DataFrame(data, columns=['user_id', 'col1', 'col2', 'col3', 'col4'])

    # Remove duplicates
    df = df.drop_duplicates()

    # Impute missing values
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].fillna(df[col].mode()[0])
        elif df[col].dtype == 'float':
            df[col] = df[col].fillna(df[col].mean())

    # Convert col3 to datetime
    df['col3'] = pd.to_datetime(df['col3'])
    
    # Extract day, month, and week from the col3 (date) column
    df['day'] = df['col3'].dt.day
    df['month'] = df['col3'].dt.month
    df['week'] = df['col3'].dt.isocalendar().week.astype('int64')

    # Convert boolean values in col1 to 0 and 1
    df['col1'] = df['col1'].astype(int)

    # Return the transformed DataFrame
    return df


def load_data(transformed_df):
    # Initialize the BigQuery client
    bigquery_client = connect_to_bigquery()

    # Define the table reference
    table_ref = bigquery_client.dataset("ml_datasets").table("mltests_v3")

    # Load the DataFrame into the BigQuery table
    load_job = bigquery_client.load_table_from_dataframe(transformed_df, table_ref)
    load_job.result()

    # Print a message to indicate the load is complete
    print("Data loaded successfully.")