import pandas as pd
import psycopg2
from google.cloud import bigquery
import common_env as ce

# Create a connection to the PostgreSQL database
conn = psycopg2.connect(
    dbname="itba-dev",
    host="localhost",
    port="5432"
)

# Create a new cursor object
cursor = conn.cursor()

# Write your SQL query to fetch data
sql = "SELECT * FROM titanic;"

# Execute the SQL command
cursor.execute(sql)

# Fetch all the rows
rows = cursor.fetchall()

# Get the column names from the cursor description
column_names = [desc[0] for desc in cursor.description]

# Convert the result to pandas DataFrame
df = pd.DataFrame(rows, columns=column_names)

conn.close()

# Create a BigQuery client
client = bigquery.Client()

# Get table reference
table_ref = client.dataset(ce.DATASET_ID).table('titanic')

# Define job config
job_config = bigquery.LoadJobConfig()
job_config.autodetect = True
job_config.write_disposition = "WRITE_TRUNCATE"  # Use "WRITE_APPEND" to append data to the existing table

# Load DataFrame to BigQuery
job = client.load_table_from_dataframe(
    df,
    table_ref,
    job_config=job_config
)

# Wait for the load job to complete
job.result()
