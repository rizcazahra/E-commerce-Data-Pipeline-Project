-- Create the dim_product table
WITH product_cte AS (
  SELECT DISTINCT
    Product_SKU AS product_id,
    Product_Description AS product_description,
    Product_Category AS product_category
  FROM {{ source('online', 'raw_invoices') }}
)

SELECT
  product_id,
  product_description,
  product_category
FROM product_cte
