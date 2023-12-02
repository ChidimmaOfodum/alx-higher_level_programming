#!/usr/bin/python3
"""Post email with get"""

if __name__ == "__main__":
    import requests
    from sys import argv

    email = {
        "email": argv[2]
    }
    r = requests.post(argv[1], email)
    print(r.text)
