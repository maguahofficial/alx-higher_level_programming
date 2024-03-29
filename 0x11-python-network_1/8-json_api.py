#!/usr/bin/python3
"""This sends a POST request to http://0.0.0.0:5000/search_user with a given letter.

  - letter is sent as the value of the variable `q`.
  - so if no letter is provided,it will send `q=""`.
"""
import sys
import requests


if __name__ == "__main__":
    letterx = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letterx}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
