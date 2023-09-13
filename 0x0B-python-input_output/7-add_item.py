#!/usr/bin/python3
from sys import argv
saveJson = __import__('5-save_to_json_file').save_to_json_file
loadJson = __import__('6-load_from_json_file').load_from_json_file

argv = argv[1:]
args = []

try:
    args = loadJson('add_item.json')
except Exception:
    with open('add_item.json', 'w') as f:
        pass
args += argv
saveJson(args, 'add_item.json')
