import get_data_from_api as my_module
from unittest.mock import patch


@patch('get_data_from_api.requests.get')
def test_get_data_from_api(mock_get):
    # Mocked JSON response
    mock_get.return_value.json.return_value = {
        "result_number": "10"
    }

    expected_output = {
        "result_number": 10
    }

    # Call the function with the mocked GET request
    actual_output = my_module.get_and_transform_data_from_api(10)

    # Assert that the mocked JSON response is equal to the expected output
    assert actual_output == expected_output, f"Expected {expected_output}, but got {actual_output}"
