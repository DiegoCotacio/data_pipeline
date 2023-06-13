from prefect import flow, task
import json
import requests
import pandas as pd
from datetime import datetime

@task
def extract(url: str) -> dict:
    res = requests.get(url)
    if not res:
        raise Exception('No data fetched!')
    return json.loads(res.content)

@task
def transform(data: dict) -> pd.DataFrame:
    transformed = []
    for user in data:
        transformed.append({
            'ID': user['id'],
            'Name': user['name'],
            'Username': user['username'],
            'Email': user['email'],
            'Address': f"{user['address']['street']}, {user['address']['suite']}, {user['address']['city']}",
            'PhoneNumber': user['phone'],
            'Company': user['company']['name']
        })
    return pd.DataFrame(transformed)

@task
def load(data: pd.DataFrame, path: str) -> None:
    data.to_csv(path_or_buf=path, index=False)

@flow(name="User Extraction Flow")
def user_extraction_flow():
    url = 'https://jsonplaceholder.typicode.com/users'
    path = f'C:/Users/diego/OneDrive/Escritorio/mlops_projects/ml/data_pipeline_project/users_{int(datetime.now().timestamp())}.csv'
    users = extract(url)
    df_users = transform(users)
    load_completed = load(data=df_users, path=path)
    return load_completed

if __name__ == '__main__':
 user_extraction_flow()