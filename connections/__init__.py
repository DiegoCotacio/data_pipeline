# Importar funciones y clases
from .bigquery_connection import connect_to_bigquery
from .postgres_connection import connect_to_postgres

# Definir funciones globales del paquete
connect = {
    "connect_to_bigquery": connect_to_bigquery,
    "connect_to_postgres": connect_to_postgres
}