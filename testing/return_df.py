import pandas as pd


def create_dataframe(n_rows=5):
    """
    This function returns a dataframe with specified number of rows. By default, the number of rows is 5.

    Arguments:
    n_rows: int, optional : The number of rows in the dataframe. (default is 5)

    Returns:
    df: pandas DataFrame
    """
    data = {
        "Column1": list(range(n_rows)),
        "Column2": ["Value" + str(i) for i in range(n_rows)],
    }
    df = pd.DataFrame(data)

    return df
