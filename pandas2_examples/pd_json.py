import pandas as pd
import requests
import json


def get_response():
    # URL of the public API you want to use
    url = "http://echo.jsontest.com/a/1/b/2/c/3"

    # Make a GET request to the REST API
    response = requests.get(url)

    # Make sure the request was successful
    response.raise_for_status()

    data = response.json()

    # Open file and write the data
    with open("output.json", "w") as outfile:
        json.dump(data, outfile)


def read_json():
    # Load json object
    with open('output.json') as f:
        data = json.load(f)

    # Flatten data because there's only one row
    df = pd.json_normalize(data)
    print(df)


if __name__ == "__main__":
    get_response()
    read_json()
