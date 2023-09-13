#!/usr/bin/python3
"""A module that defines class_to_json"""
import json


def class_to_json(obj):
    result = {}
    for i in dir(obj):
        if i[:2] != '__':
            att = getattr(obj, i)
            try:
                json.dumps(att)
                result[i] = att
            except:
                pass
    return result
