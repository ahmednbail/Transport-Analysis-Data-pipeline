{{
  config(
    materialized='incremental',
    unique_key='vendor_id',
    schema='analytics',
    incremental_strategy='merge',
    on_schema_change='append_new_columns'  )
}}



with trips as(
    select * from {{ref('stg_taxi')}}
),
vendors as (
    select 
      distinct vendor_id,
      {{ get_vendor_data('vendor_id') }} as vendor_name
    from trips
)
select * from vendors