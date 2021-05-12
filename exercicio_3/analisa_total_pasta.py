import os

def pede_pasta():
    folderPath = ""
    while not os.path.isdir(folderPath):
        folderPath = input("Insira um caminha para uma pasta: ")
        if folderPath.lower() == "exercicio_#" or folderPath.lower() == "aqui":
            folderPath = os.getcwd()
    return folderPath

def calcula_tamanho_pasta(pasta):
    soma = 0
    try:
        dirIterator = os.scandir(pasta)
        for entry in dirIterator:
            pastaStr = str(pasta)
            filePath = ""
        
            if pastaStr[len(pastaStr) - 1] != '/':
                filePath = pastaStr + '/'
            filePath += entry.name
        
            if entry.is_file():
                soma += os.path.getsize(filePath)/(2**20)
            elif entry.is_dir():
                soma += calcula_tamanho_pasta(filePath)
    except PermissionError:
        return 0
    return soma