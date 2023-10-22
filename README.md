# Bigmart-Data-Pipeline-Project
<img width="781" alt="Bigmart" src="https://github.com/rizcazahra/Bigmart-Data-Pipeline-Project/assets/84758353/a144b5e4-5a51-44c1-8082-c1635e7b7d8e">

This project is designed to create a data pipeline for processing and analyzing sales data from Bigmart, sourced from [Kaggle](https://www.kaggle.com/datasets/brijbhushannanda1979/bigmart-sales-data). The pipeline uses:
1. Astro CLI: Used for managing and orchestrating data workflows.
2. Apache Airflow: Orchestrates the data pipeline tasks.
3. Google Cloud Storage: Stores the raw and processed data.
4. Google BigQuery: Acts as the data warehousing solution for querying and analyzing the data.
5. Docker: Manages application dependencies and ensures consistent environments.
6. Metabase: Provides a user-friendly interface for reporting and data visualization.

## Project Overview

- **DAG**: The project includes an Apache Airflow Directed Acyclic Graph (DAG) named "bigmart" that defines the workflow of the data pipeline.
- **Data Source**: The source data is stored in a CSV file, `bigmart_sales.csv`, located in the `include/dataset/` directory.
- **Data Destination**: Processed data is stored in Google BigQuery under the `bigmart` dataset.
- **Connections**: The project relies on a Google Cloud Storage (GCS) connection (connection ID: `gcp`) for uploading and accessing data, as well as a Google BigQuery connection (connection ID: `gcp`) for interacting with BigQuery.

## Prerequisites

Before running the data pipeline, ensure you have the following prerequisites:

- [Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/start/index.html) is set up and configured.
- [Google Cloud Storage (GCS)](https://cloud.google.com/storage) and [Google BigQuery](https://cloud.google.com/bigquery) are set up and authenticated.
- [Docker](https://www.docker.com/) is installed and running.

## Getting Started

### 1. Clone the Repository

git clone <repository_url>
cd <repository_directory>

### 2. Build the Docker Image
docker build -t bigmart-data-pipeline .

### 3. Run the Docker Container
docker run -d -p 8080:8080 --name bigmart-pipeline bigmart-data-pipeline

### 4. Access the Airflow Web Interface
Visit http://localhost:8080 in your web browser to access the Apache Airflow web interface.

### 5. Configure Connections
In the Airflow web interface, navigate to the "Admin" section and select "Connections." Configure the following connections:

gcp: Configure a Google Cloud Platform connection with the necessary credentials.

### 6. Run the DAG
In the Airflow web interface, navigate to the "DAGs" section and find the "bigmart" DAG. Trigger the DAG to start the data pipeline.

DAG Tasks

upload_csv_to_gcs: Uploads the CSV data file to Google Cloud Storage (raw/bigmart_sales.csv).
create_bigmart_dataset: Creates an empty dataset named bigmart in Google BigQuery.
gcs_to_raw: Loads data from Google Cloud Storage into a BigQuery table named raw_invoices under the bigmart dataset.
Visualizing Data with Metabase

After the data pipeline has run successfully, you can visualize the processed data using Metabase. You can connect Metabase to Google BigQuery to create visualizations and dashboards.

