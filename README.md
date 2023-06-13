# README.md

This repository contains a data pipeline for an ETL batch that extracts data from a PostgreSQL table, transforms it, and loads it into a BigQuery table. The pipeline is executed every 1 hour using GitHub Actions.

To use this repository:

1. Clone the repository
2. Install the required Python packages: pip install -r requirements.txt
3. Configure the `configuration.yml` file with your PostgreSQL and BigQuery credentials
4. Commit and push the changes to GitHub
5. The data pipeline will be executed every 1 hour by GitHub Actions