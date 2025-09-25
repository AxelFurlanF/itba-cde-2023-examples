import requests


def get_data_from_api(num):
    """
    This function sends GET request to specified URL and return the JSON response

    Arguments:
    url : str : The URL where the GET request will be sent.

    Returns:
    dict : The JSON response received from the GET request.
    """
    url = f'http://echo.jsontest.com/result_number/{num}'
    response = requests.get(url)
    return response.json()


def get_and_transform_data_from_api(num):
    """
    This function sends GET request to specified URL and return the JSON response

    Arguments:
    url : str : The URL where the GET request will be sent.

    Returns:
    dict : The JSON response received from the GET request.
    """
    data = get_data_from_api(num)

    data['result_number'] = int(data['result_number'])
    return data
