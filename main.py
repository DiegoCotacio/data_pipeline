from etl.etl_functions import extract_data, transform_data, load_data
from connections.postgres_connection import connect_to_postgres
from connections.bigquery_connection import connect_to_bigquery

def postgres_to_bigquery_pipeline():
    # Connect to PostgreSQL
    data = extract_data()

    # Transform the data
    transformed_data = transform_data(data)

    # Load the data into BigQuery
    load_data(transformed_data)

if __name__ == "__main__":
    postgres_to_bigquery_pipeline()