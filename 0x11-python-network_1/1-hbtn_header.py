#!/usr/bin/python3
"""Displays response headers"""
if __name__ == "__main__":
    from sys import argv
    from urllib import request

    with request.urlopen(argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
