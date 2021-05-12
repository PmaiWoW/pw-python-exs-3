import string

def calcula_linhas(filename):
    lineNum = 0
    try:
        with open(filename) as file:
            for line in file:
                lineNum += 1
    except OSError:
        print("Could not open/read file, please check the name inserted.")
        return
    return lineNum

def calcula_carateres(filename):
    charNum = 0
    try:
        with open(filename) as file:
            for line in file:
                charNum = charNum + len(line)
    except OSError:
        print("Could not open/read file, please check the name inserted.")
        return
    return charNum

def calcula_palavra_comprida(filename):
    longestWord = ""
    try:
        with open(filename) as file:
            for line in file:
                wordsList = line.split()
                for word in wordsList:
                    if len(word) > len(longestWord):
                        longestWord = word
    except OSError:
        print("Could not open/read file, please check the name inserted.")
        return
    return longestWord

def calcula_ocorrencia_de_letras(filename):
    chars = dict.fromkeys(string.ascii_lowercase, 0)
    try:
        with open(filename) as file:
            for line in file:
                for char in line:
                    lowerChar = char.lower()
                    if lowerChar.isalpha():
                        chars[lowerChar] = chars[lowerChar] + 1
    except OSError:
        print("Could not open/read file, please check the name inserted.")
        return
    return chars