#!/usr/bin/env python
import argparse
import requests

def main(url):

        KERAS_REST_API_URL = "http://127.0.0.1:45000/predict"

        payload = {"url": url}

        r = requests.post(KERAS_REST_API_URL, json=payload)
        response = r.json()

        if response["success"]:
                print(response['predictions'])

        else:
                print("Request failed")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Rock and roll.')
    parser.add_argument(
        '-u',
        dest='url',
        action='store',
        required=True,
        help="This is the url."
    )

    args = parser.parse_args()

    main(**vars(args))


