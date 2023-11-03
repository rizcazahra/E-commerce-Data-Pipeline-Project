SELECT
  customer_id,
  gender,
  location,
  tenure_months
FROM {{ source('online', 'country') }}