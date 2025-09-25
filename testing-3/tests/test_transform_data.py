from my_package import get_data_from_api as my_module
from unittest.mock import patch, Mock, MagicMock


def test_get_api_data_with_mocks():
    # Create a mock response object with a .json() method
    mock_response = MagicMock()

    # Set the .json() method to return a specific dictionary
    mock_response.json.return_value = {"result_number": "10"}

    # Mock requests.get to return the mock_response
    my_module.requests.get = Mock(return_value=mock_response)

    # Call the function - instead of calling requests.get(),
    # it will call the mock, which returns mock_response,
    # which has a .json() method that returns the test dictionary
    data = my_module.get_and_transform_data_from_api(10)

    # Assert the function returns the correct data
    assert data == {"result_number": 10}


@patch("my_package.get_data_from_api.requests.get")
def test_get_data_from_api_with_patch(mock_get):
    # Mocked JSON response
    # get().json()
    mock_get.return_value.json.return_value = {"result_number": "10"}

    expected_output = {"result_number": 10}

    # Call the function with the mocked GET request
    actual_output = my_module.get_and_transform_data_from_api(10)

    # Assert that the mocked JSON response is equal to the expected output
    assert (
        actual_output == expected_output
    ), f"Expected {expected_output}, but got {actual_output}"
