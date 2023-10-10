import pandas as pd
import time

start = time.time()
pd.read_parquet('big_titanic.parquet')
end = time.time()

read_time = end - start
print(read_time)

start = time.time()
pd.read_parquet('big_titanic_sin_gzip.parquet')
end = time.time()

read_time = end - start
print(read_time)
