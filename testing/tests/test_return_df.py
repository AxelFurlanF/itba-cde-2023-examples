import pandas as pd
import return_df as my_module


def test_create_dataframe():
    # set up
    expected_output = pd.DataFrame(data={"Column1": [0, 1, 2, 3, 4], "Column2": [
                                   "Value0", "Value1", "Value2", "Value3", "Value4"]})

    # action
    actual_output = my_module.create_dataframe()

    # assert
    pd.testing.assert_frame_equal(actual_output, expected_output)
