import pandas as pd
import time
import os


def read_titanic_csv():
    df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
    return df


def to_parquet(df, name):
    df.to_parquet(name)


def multiply_dataset(df, n=1000):
    df = pd.concat([df] * n, ignore_index=True)
    return df


def compare_file_efficiency(csv_path, parquet_path):
    # Measure the time taken to read the CSV file
    start = time.time()
    pd.read_csv(csv_path)
    end = time.time()
    csv_read_time = end - start

    # Measure the time taken to read the Parquet file
    start = time.time()
    pd.read_parquet(parquet_path)
    end = time.time()
    parquet_read_time = end - start

    # Measure the time taken to read just a column
    start = time.time()
    pd.read_parquet(parquet_path, columns=['Pclass'])
    end = time.time()
    column_read_time = end - start

    # Get the file sizes in megabytes
    csv_size = os.path.getsize(csv_path) / (1024 * 1024)
    parquet_size = os.path.getsize(parquet_path) / (1024 * 1024)

    print(f'CSV file read time: {csv_read_time} seconds')
    print(f'Parquet file read time: {parquet_read_time} seconds\n')
    print(f'Parquet just one column: {column_read_time} seconds\n')
    print(f'Efficiency is: {csv_read_time / parquet_read_time} times faster')

    print(f'CSV file size: {csv_size} megabytes')
    print(f'Parquet file size: {parquet_size} megabytes')
    print(f'Parquet is {csv_size / parquet_size} times smaller')


if __name__ == "__main__":
    print('------------SMALL FILE------------')
    df = read_titanic_csv()
    df.to_csv('titanic.csv', index=False)
    to_parquet(df, 'titanic.parquet')
    compare_file_efficiency('titanic.csv', 'titanic.parquet')

    df = multiply_dataset(df)

    print('------------BIG FILE------------')
    df.to_csv('big_titanic.csv', index=False)
    to_parquet(df, 'big_titanic.parquet')
    compare_file_efficiency('big_titanic.csv', 'big_titanic.parquet')
