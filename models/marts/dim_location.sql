{{
  config(
    materialized='incremental',
    unique_key='location_id',
    schema='analytics',
    incremental_strategy='merge',
    on_schema_change='append_new_columns'  )
}}


with taxi_zone_lookup as (
    select * from {{ref(
        'taxi_zone_lookup'
    )}}
),
renamed as(
    select 
        locationid as location_id,
        borough,
        zone,
        service_zone
    from taxi_zone_lookup
 
)

select * from renamed