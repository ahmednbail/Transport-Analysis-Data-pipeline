import pandas as pd 
from tqdm.auto import tqdm
from sqlalchemy import create_engine
import click

dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

@click.command()
@click.option('--pg_user', default='postgres', help='Postgres User')
@click.option('--pg_password', default='postgres123', help='Postgres Password')
@click.option('--pg_host', default='localhost', help='Postgres Host')
@click.option('--pg_port', default=5433, help='Postgres Port')
@click.option('--pg_db', default='ny_taxi', help='Postgres Database')
@click.option('--chunksize', default=100000, help='Chunk size for processing')
@click.option('--target_table', default='yellow_taxi_data', help='Target table name')
def run(pg_user, pg_password, pg_host, pg_port, pg_db,chunksize, target_table): 

        
        url=r"D:\Ahmed\Projects\Transport-Analysis-Data-pipeline\Data\yellow_tripdata_2021-01.csv"
        engine=create_engine(f'postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}')

        df_iter=pd.read_csv(
            url,
            dtype=dtype,
            parse_dates=parse_dates,
            iterator= True,
            chunksize=chunksize,
        )

        first=True
        for df_chunk in tqdm(df_iter):
            if first:
                df_chunk.head(0).to_sql(
                    name=target_table,
                    con=engine,
                    if_exists='replace'
                )
                first = False
            df_chunk.to_sql(
                name=target_table,
                con=engine,
                if_exists='append'
            )

if __name__ == '__main__':
    run()

