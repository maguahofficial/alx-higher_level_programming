#!/usr/bin/python3
"""This List 10 most recent commits on a given GitHub repository.

"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    r = requests.get(url)
    commits = r.json()
    try:
        for ixx in range(10):
            print("{}: {}".format(
                commits[ixx].get("sha"),
                commits[ixx].get("commit").get("author").get("name")))
    except IndexError:
        pass
