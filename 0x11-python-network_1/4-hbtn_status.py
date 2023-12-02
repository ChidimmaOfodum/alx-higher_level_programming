#!/usr/bin/python3
"""Using request module"""

if __name__ == "__main__":
    import requests

    r = requests.get("https://alx-intranet.hbtn.io/status").text
    print("Body response:")
    print("\t- type: {}".format(type(r)))
    print("\t- content: {}".format(r))
