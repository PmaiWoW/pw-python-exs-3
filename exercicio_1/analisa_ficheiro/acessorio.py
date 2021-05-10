import os
import json

def pede_nome(filename):
    fname = ""
    if not filename.endswith(".txt"):
        print("Name invalid, must be a txt file.")
        return
    try:
        with open(filename, 'r') as file:
            fname = f.name
    except OSError:
        print("Could not open/read the file, please check the name inserted.")
        return
    return fname

def gera_nome(filename):
    if not filename.endswith(".txt"):
        print("Name invalid, must be a txt file.")
        return
    try:
        f = open(filename, "r")
    except OSError:
        print("Could not find file, please check the name inserted.")
        return
    jsonname = filename.split('.')[0]
    with open(jsonname, 'w') as jsonFile:
        json.dump(pessoa_dict, jsonFile, indent = 4)
    return