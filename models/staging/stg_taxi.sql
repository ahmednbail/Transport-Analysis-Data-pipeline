select
    -- identifiers
    vendorid as vendor_id,
    ratecodeid as rate_code_id,
    pulocationid as pickup_location_id,
    dolocationid as dropoff_location_id,

    -- timestamp
    tpep_pickup_datetime as pickup_datetime,
    tpep_dropoff_datetime as dropoff_datetime,

    -- trip info
    store_and_fwd_flag,
    passenger_count,
    trip_distance,

    -- payment_info
    payment_type,
    cast(fare_amount as numeric) as fare_amount,
    cast(extra as numeric) as extra,
    cast(mta_tax as numeric) as mta_tax,
    cast(tip_amount as numeric) as tip_amount,
    cast(tolls_amount as numeric) as tolls_amount,
    cast(improvement_surcharge as numeric) as improvement_surcharge,
    cast(total_amount as numeric) as total_amount,
    cast(congestion_surcharge as numeric) as congestion_surcharge

from {{ source("transport-analysis", "yellow_tripdata") }}
where VendorID is not null  