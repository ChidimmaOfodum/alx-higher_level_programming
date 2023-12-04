#!/usr/bin/python3
"""A post request with params"""

if __name__ == "__main__":
    from sys import argv
    import requests

    q = {
        "q": argv[1]
    }

    r = requests.post('http://0.0.0.0:5000/search_user', q)
    try:
        r = eval(r.content.decode('utf-8'))
        if bool(r):
            print("[{}] {}".format(r.get('id'), r.get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
