from airflow.decorators import dag, task
from datetime import datetime

from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateEmptyDatasetOperator
from astro import sql as aql
from astro.files import File
from astro.sql.table import Table, Metadata
from astro.constants import FileType
from include.dbt.cosmos_config import DBT_PROJECT_CONFIG, DBT_CONFIG
from cosmos.airflow.task_group import DbtTaskGroup
from cosmos.constants import LoadMode
from cosmos.config import ProjectConfig, RenderConfig

@dag(
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False,
    tags=['online'],
)
def retail():

    upload_csv_to_gcs = LocalFilesystemToGCSOperator(
        task_id='upload_csv_to_gcs',
        src='include/dataset/online_sales.csv',
        dst='raw/online_sales.csv',
        bucket='rizcaz_bigmart_sales',
        gcp_conn_id='gcp',
        mime_type='text/csv',
    )

    upload_csv_to_gcs_two = LocalFilesystemToGCSOperator(
        task_id='upload_csv_to_gcs_two',
        src='include/dataset/marketing_spend.csv',
        dst='raw/marketing_spend.csv',
        bucket='rizcaz_bigmart_sales',
        gcp_conn_id='gcp',
        mime_type='text/csv',
    )

    upload_csv_to_gcs_three = LocalFilesystemToGCSOperator(
        task_id='upload_csv_to_gcs_three',
        src='include/dataset/discount_coupon.csv',
        dst='raw/discount_coupon.csv',
        bucket='rizcaz_bigmart_sales',
        gcp_conn_id='gcp',
        mime_type='text/csv',
    )

    upload_csv_to_gcs_four = LocalFilesystemToGCSOperator(
        task_id='upload_csv_to_gcs_four',
        src='include/dataset/customer_data.csv',
        dst='raw/customer_data.csv',
        bucket='rizcaz_bigmart_sales',
        gcp_conn_id='gcp',
        mime_type='text/csv',
    )

    upload_csv_to_gcs_five = LocalFilesystemToGCSOperator(
        task_id='upload_csv_to_gcs_five',
        src='include/dataset/task_amount.csv',
        dst='raw/customer_data.csv',
        bucket='rizcaz_bigmart_sales',
        gcp_conn_id='gcp',
        mime_type='text/csv',
    )
    create_online_dataset = BigQueryCreateEmptyDatasetOperator(
        task_id='create_online_dataset',
        dataset_id='online',
        gcp_conn_id='gcp',
    )

    gcs_to_raw = aql.load_file(
        task_id='gcs_to_raw',
        input_file=File(
            'gs://rizcaz_bigmart_sales/raw/online_sales.csv',
            conn_id='gcp',
            filetype=FileType.CSV,
        ),
        
        output_table=Table(
            name='raw_invoices',
            conn_id='gcp',
            metadata=Metadata(schema='online')
        ),
        use_native_support=False,
    )

    gcs_to_raw_two = aql.load_file(
        task_id='gcs_to_raw_two',
        input_file=File(
            'gs://rizcaz_bigmart_sales/raw/marketing_spend.csv',
            conn_id='gcp',
            filetype=FileType.CSV,
        ),
        
        output_table=Table(
            name='marketing_spend',
            conn_id='gcp',
            metadata=Metadata(schema='online')
        ),
        use_native_support=False,
    )

    gcs_to_raw_three = aql.load_file(
        task_id='gcs_to_raw_three',
        input_file=File(
            'gs://rizcaz_bigmart_sales/raw/discount_coupon.csv',
            conn_id='gcp',
            filetype=FileType.CSV,
        ),
        
        output_table=Table(
            name='discount_coupon',
            conn_id='gcp',
            metadata=Metadata(schema='online')
        ),
        use_native_support=False,
    )

    gcs_to_raw_four = aql.load_file(
        task_id='gcs_to_raw_four',
        input_file=File(
            'gs://rizcaz_bigmart_sales/raw/customer_data.csv',
            conn_id='gcp',
            filetype=FileType.CSV,
        ),
        
        output_table=Table(
            name='marketing_spend',
            conn_id='gcp',
            metadata=Metadata(schema='online')
        ),
        use_native_support=False,
    )

    gcs_to_raw_five = aql.load_file(
        task_id='gcs_to_raw_five',
        input_file=File(
            'gs://rizcaz_bigmart_sales/raw/tax_amount.csv',
            conn_id='gcp',
            filetype=FileType.CSV,
        ),
        
        output_table=Table(
            name='marketing_spend',
            conn_id='gcp',
            metadata=Metadata(schema='online')
        ),
        use_native_support=False,
    )

    @task.external_python(python='/usr/local/airflow/soda_venv/bin/python')
    def check_load(scan_name='check_load', checks_subpath='sources'):
        from include.soda.check_function import check
        
        return check(scan_name, checks_subpath)
    
    check_load()

    transform = DBTaskGroup(
        group_id='transform',
        project_config=DBT_PROJECT_CONFIG,
        profile_config=DBT_CONFIG,
        render_config=RenderConfig(
            load_method=LoadMode.DBT_LS,
            select=['path:models/transform']
        )
    )

retail()
