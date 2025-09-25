import pandas as pd


def create_dataframe():
    """
    Creates a simple DataFrame with two columns.

    Returns:
    pd.DataFrame: A DataFrame with Column1 containing integers 0-4
                  and Column2 containing corresponding value strings.
    """
    return pd.DataFrame(
        data={
            "Column1": [0, 1, 2, 3, 4],
            "Column2": ["Value0", "Value1", "Value2", "Value3", "Value4"],
        }
    )
