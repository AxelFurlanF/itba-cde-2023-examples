from my_package import get_data_from_api
from unittest.mock import patch, Mock, MagicMock


def test_get_api_data_with_mocks():
    # Create a mock response object with a .json() method
    mock_response = MagicMock()

    # Set the .json() method to return a specific dictionary
    mock_response.json.return_value = {"example": "axel", "method": "GET"}

    get_data_from_api.requests.get = Mock(return_value=mock_response)

    data = get_data_from_api.get_and_transform_data_from_api()

    assert data == {"example": "axel", "method": "get"}


@patch("my_package.get_data_from_api.requests.get")
def test_get_data_from_api_with_patch(mock_get):
    mock_get.return_value.json.return_value = {"example": "axel", "method": "GET"}

    data = get_data_from_api.get_and_transform_data_from_api()

    assert data == {"example": "axel", "method": "get"}
