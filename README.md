# Bigmart-Data-Pipeline-Project

This project is designed to create a data pipeline for processing and analyzing sales data from Bigmart, sourced from [Kaggle](https://www.kaggle.com/datasets/brijbhushannanda1979/bigmart-sales-data). The pipeline uses Apache Airflow for orchestration, Google Cloud Storage for data storage, and Google BigQuery for data warehousing. The processed data can then be visualized using Metabase.

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

```bash
git clone <repository_url>
cd <repository_directory>

### 2. Build the Docker Image
```bash
Copy code
docker build -t bigmart-data-pipeline .

### 3. Run the Docker Container
```bash
Copy code
docker run -d -p 8080:8080 --name bigmart-pipeline bigmart-data-pipeline

### 4. Access the Airflow Web Interface
Visit http://localhost:8080 in your web browser to access the Apache Airflow web interface.

5. Configure Connections
In the Airflow web interface, navigate to the "Admin" section and select "Connections." Configure the following connections:

gcp: Configure a Google Cloud Platform connection with the necessary credentials.

6. Run the DAG
In the Airflow web interface, navigate to the "DAGs" section and find the "bigmart" DAG. Trigger the DAG to start the data pipeline.

DAG Tasks

upload_csv_to_gcs: Uploads the CSV data file to Google Cloud Storage (raw/bigmart_sales.csv).
create_bigmart_dataset: Creates an empty dataset named bigmart in Google BigQuery.
gcs_to_raw: Loads data from Google Cloud Storage into a BigQuery table named raw_invoices under the bigmart dataset.
Visualizing Data with Metabase

After the data pipeline has run successfully, you can visualize the processed data using Metabase. You can connect Metabase to Google BigQuery to create visualizations and dashboards.

