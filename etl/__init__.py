# Importar funciones y clases de etl_functions.py y data_modeling.py
from .etl_functions import extract_data, transform_data, load_data

# Definir funciones globales del paquete etl
etl = {
    "extract_data": extract_data,
    "transform_data": transform_data,
    "load_data": load_data
}