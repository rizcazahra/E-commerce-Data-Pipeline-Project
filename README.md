# Bigmart-Data-Pipeline-Project
<img width="1305" alt="image" src="https://github.com/rizcazahra/E-commerce-Data-Pipeline-Project/assets/84758353/f59cb405-a862-4459-bf39-97e6fff8e953">

In this project, we will undertake an end-to-end data engineering endeavor. We will utilize a financial dataset from [Kaggle][(https://www.kaggle.com/datasets/rishikumarrajvansh/marketing-insights-for-e-commerce-company?select=Online_Sales.csv)] to unearth meaningful insights by examining the data's trends and patterns. The project scope encompasses the following tasks:
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
- **Data Source**: The data have 6 sources: Discount_Coupon.csv, Marketing_Spend.csv, Tax_amount.xlsx, CustomersData.xlsx and Online_Sales.csv, located in the `include/dataset/` directory.
- **Data Destination**: Processed data is stored in Google BigQuery under the `online` dataset.
- **Connections**: The project relies on a Google Cloud Storage (GCS) connection (connection ID: `gcp`) for uploading and accessing data, as well as a Google BigQuery connection (connection ID: `gcp`) for interacting with BigQuery.

## Prerequisites

Before running the data pipeline, ensure you have the following prerequisites:

- Google Cloud Account.
- [Docker](https://www.docker.com/) is installed and running.
- [Astro CLI](https://docs.astronomer.io/astro/cli/overview)
   
## Getting Started

