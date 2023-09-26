import pandas as pd


def write_partitioned_files():
    df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
    df.to_parquet('parquet_partitions/titanic', partition_cols=['Pclass'])


def read_partitioned_files():
    df = pd.read_parquet('titanic.parquet', engine='pyarrow', filters=[('Pclass', '=', 1)])
    print(df)


if __name__ == "__main__":
    write_partitioned_files()
    read_partitioned_files()
