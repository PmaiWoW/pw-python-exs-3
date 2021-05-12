import os
import json
import io

def pede_nome(filename):
    fname = ""
    if not filename.endswith(".txt"):
        print("Name invalid, must be a txt file.")
        return
    try:
        with open(filename, 'r') as file:
            fname = file.name
    except OSError:
        print("Could not open/read the file, please check the name inserted.")
        return
    return fname

def gera_nome(filename):
    if not filename.endswith(".txt"):
        print("Name invalid, must be a txt file.")
        return
    try:
        with open(filename, 'r') as txtFile:
            fileContent = txtFile.readlines()
            jsonname = filename.split('.')[0] + ".json"
            with open(jsonname, 'w') as jsonFile:
                personality_dict = {}
                for line in fileContent:
                    name = line.split(';')[0].split(':')[1]
                    classes = line.split(';')[1].split(':')[1].split(',')
                    age = line.split(';')[2].split(':')[1]
                    personality_dict = { "Name":name, "Classes":classes, "Age":int(age) }
                json.dump(personality_dict, jsonFile, indent=4, sort_keys=True)
    except OSError:
        print("Could not find file, please check the name inserted.")
        return
    return jsonFile.name