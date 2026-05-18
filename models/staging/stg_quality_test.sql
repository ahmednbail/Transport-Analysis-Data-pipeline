select count(*) 
from {{source('transport-analysis','yellow_tripdata')}}