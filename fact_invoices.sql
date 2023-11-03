-- Create the fact_invoices_cte by joining the relevant keys from dimension tables
WITH fact_invoices_cte AS (
  SELECT
    r.CustomerID AS customer_id,
    r.Transaction_ID AS transaction_id,
    p.product_id,
    r.Quantity AS quantity,
    r.Avg_Price AS avg_price,
    r.Delivery_Charges AS delivery_charges,
    r.Coupon_Status AS coupon_status,
    r.Product_Category as product_category,
    t.transaction_date
  FROM {{ source('online', 'raw_invoices') }} AS r
  LEFT JOIN {{ ref('dim_product') }} AS p
    ON r.Product_SKU = p.product_id
  LEFT JOIN {{ ref('dim_datetime') }} AS t
    ON DATE(r.Transaction_Date) = t.transaction_date
  LEFT JOIN {{ ref('dim_customer') }} AS c
    ON r.CustomerID = c.customer_id
)

-- Create the fact_invoices table by selecting relevant columns from the fact_invoices_cte
SELECT
  customer_id,
  transaction_date,
  transaction_id,
  product_id,
  quantity,
  avg_price,
  delivery_charges,
  coupon_status,
  product_category
FROM fact_invoices_cte