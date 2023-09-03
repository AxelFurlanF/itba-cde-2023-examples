import pandas as pd


def test_get_example_df():
    from mymodule.somefunctions import get_example_df
    df = get_example_df()
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 2)
    assert df['a'].sum() == 6
    assert df['b'].sum() == 15
