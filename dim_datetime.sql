-- Create the dim_datetime table 
WITH datetime_cte AS (  
  SELECT DISTINCT
    PARSE_DATE('%m/%d/%Y', Transaction_Date) AS transaction_date,
    transaction_id
  FROM {{ source('online', 'raw_invoices') }}
)

-- Extract date and time components in a separate SELECT statement
SELECT
  transaction_id,
  transaction_date,
  EXTRACT(YEAR FROM transaction_date) AS year,
  EXTRACT(MONTH FROM transaction_date) AS month,
  EXTRACT(DAY FROM transaction_date) AS day,
  EXTRACT(DAYOFWEEK FROM transaction_date) AS day_of_week,
  EXTRACT(DAYOFYEAR FROM transaction_date) AS day_of_year
FROM datetime_cte