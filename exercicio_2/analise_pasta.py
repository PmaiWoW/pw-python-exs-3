import os
from matplotlib import pyplot as plt
import csv

def pede_pasta():
    folderPath = ""
    while not os.path.isdir(folderPath):
        folderPath = input("Insira um caminha para uma pasta: ")
        if folderPath.lower() == "this file" or folderPath.lower() == "este ficheiro":
            folderPath = os.getcwd()
    return folderPath
    
def faz_calculos(fullPath):
    typeDict = {}
    dirIterator = os.scandir(fullPath)
    for entry in dirIterator:
        if entry.is_file():
            filePath = fullPath + '/' + entry.name
            kBsize = os.path.getsize(filePath)/1024
            splitName = entry.name.split('.')
            fileExt = splitName[len(splitName) - 1]
            if fileExt in typeDict:
                typeDict[fileExt]["Quantidade"] += 1
                typeDict[fileExt]["Volume(kB)"] += kBsize
            else:
                fileTypeDict = { "Quantidade": 1, "Volume(kB)": kBsize}
                typeDict[fileExt] = fileTypeDict
    return typeDict
        
def guarda_resultados(filesDict):
    with open("results.csv", 'w', newline='') as resultsCSV:
        dictKeys = list(filesDict.keys())
        campos = ["Tipo", "Quantidade", "Volume(kB)"]
        writer = csv.DictWriter(resultsCSV, fieldnames=campos)
        writer.writeheader()
        csvDict = {}
        for key in dictKeys:
            csvDict[key] = {"Tipo":key, "Quantidade": filesDict[key]["Quantidade"], "Volume(kB)": filesDict[key]["Volume(kB)"]}
        for key in csvDict:
            writer.writerow(csvDict[key])
    print(resultsCSV.name)
    return

def faz_grafico_queijos(titulo, lista_chaves, lista_valores):
    plt.pie(lista_valores, labels=lista_chaves, autopct='%1.0f%%')
    plt.title(titulo)
    plt.show()
    
def faz_grafico_barras(titulo, lista_chaves, lista_valores):
    plt.bar(lista_chaves, lista_valores)
    plt.title(titulo)
    plt.show()
