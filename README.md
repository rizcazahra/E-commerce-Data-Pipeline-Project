# Bigmart-Data-Pipeline-Project
<img width="1305" alt="image" src="https://github.com/rizcazahra/E-commerce-Data-Pipeline-Project/assets/84758353/f59cb405-a862-4459-bf39-97e6fff8e953">

In this project, we will undertake an end-to-end data engineering endeavor. We will utilize a financial dataset from Kaggle to unearth meaningful insights by examining the data's trends and patterns. The project scope encompasses the following tasks:
1. Uploading the CSV files from Kaggle to Google Cloud Storage.
2. Creating a dataset in BigQuery.
3. Moving data from Google Cloud Storage to raw format.
4. Data transformation using DBT.
5. Visualizing the data using Metabase.

The pipeline uses:
1. Astro CLI: Used for managing and orchestrating data workflows.
2. Apache Airflow: Orchestrates the data pipeline tasks.
3. Google Cloud Storage: Stores the raw data.
4. Google BigQuery: Acts as the data warehousing solution for querying and analyzing the data.
5. Docker: Manages application dependencies and ensures consistent environments.
6. Metabase: Provides a user-friendly interface for reporting and data visualization.


## Project Overview

- **DAG**: The project includes an Apache Airflow Directed Acyclic Graph (DAG) named "retail" that defines the workflow of the data pipeline.
- **Data Source**: The data have 6 sources: discount_coupon.csv, marketing_spend.csv, Tax_amount.xlsx, customer_data.csv and Online_Sales.csv, located in the `include/dataset/` directory.
- **Data Destination**: Processed data is stored in Google BigQuery under the `online` dataset.
- **Connections**: The project relies on a Google Cloud Storage (GCS) connection (connection ID: `gcp`) for uploading and accessing data, as well as a Google BigQuery connection (connection ID: `gcp`) for interacting with BigQuery.

## Prerequisites

Before running the data pipeline, ensure you have the following prerequisites:

- Google Cloud Account.
- [Docker](https://www.docker.com/) is installed and running.
- [Astro CLI](https://docs.astronomer.io/astro/cli/overview)
   
## Getting Started

- Open the Terminal on VSCode and write <code>astro dev init</code> to initialize airflow development environment
- Open the Dockerfile and write <code>quay.io/astronomer/astro-runtime:8.8.0</code> Astro CLI is a wrapper around docker, so we use that Docker image.
- Download the dataset https://www.kaggle.com/datasets/rishikumarrajvansh/marketing-insights-for-e-commerce-company?select=Online_Sales.csv store in:
   * include/dataset/online_sales.csv
   * include/dataset/marketing_spend.csv
   * include/dataset/discount_coupon.csv
   * include/dataset/customer_data.csv
   * include/dataset/tax_amount.csv
- In requirements.txt, add apache-airflow-providers-google==10.3.0 restart Airflow
- Create a GCS bucket with a unique name
- Create a service account 
   * Grant admin access to GCS + BigQuery
   * Click on the service account → Keys → Add Key → Copy the JSON content
   * Create a new file `service_account.json` in `include/gcp/`
- Airflow → Admin → Connections
  * id: gcp
  * type: Google Cloud
   * Keypath Path: `/usr/local/airflow/include/gcp/service_account.json`
- Create the DAG (retail.py)
- Test the task
  * <code>astro dev bash</code>
  * <code>airflow tasks test retail upload_csv_to_gcs 2023-01-01</code>
- Create an empty dataset on Bigquery using <code>from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyDatasetOperator</code>
- Create the task to load the file into a BigQuery
- **Data Loaded into the Warehouse**

**Transform**
- Install Cosmos - DBT
   * In requirements.txt
     <code>
     // REMOVE apache-airflow-providers-google==10.3.0
     // REMOVE soda-core-bigquery==3.0.45
     astronomer-cosmos[dbt-bigquery]==1.0.3 // install google + cosmos + dbt
     protobuf==3.20.0</code>
  * In env <code>PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python</code>
  * In Dockerfile install dbt into a virtual environment
  * Restart <code>astro dev restart</code>

- Create <code>include/dbt</code> then make packages.yml, dbt_project.yml, profiles.yml inside it
- Create sources.yml in <code>models/sources</code>
- In models/transform create dim_customer.sql, dim_datetime.sql, dim_product.sql, fact_invoices.sql
- Run the models <code>
astro dev bash
source /usr/local/airflow/dbt_venv/bin/activate
cd include/dbt
dbt deps
dbt run --profiles-dir /usr/local/airflow/include/dbt/</code>

**Visualization**
- Create a docker-compose.override.yml

<img width="1434" alt="Screenshot 2023-11-03 at 15 50 53" src="https://github.com/rizcazahra/E-commerce-Data-Pipeline-Project/assets/84758353/511c3d24-bf91-4835-a84c-3de72569a62d"> 

