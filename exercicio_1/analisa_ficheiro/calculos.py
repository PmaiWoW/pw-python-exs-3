import string

def calcula_linhas(filename):
    lineNum = 0
    if not filename.endswith(".txt"):
        print("Name invalid, must be a txt file.")
        return
    try:
        with open(filename) as file:
            for line in file:
                pass
    except OSError:
        print("Could not open/read file, please check the name inserted.")
        return
    lineNum = i
    return lineNum

def calcula_carateres(filename):
    charNum = 0
    if not filename.endswith(".txt"):
        print("Name invalid, must be a txt file.")
        return
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
    if not filename.endswith(".txt"):
        print("Name invalid, must be a txt file.")
        return
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
    if not filename.endswith(".txt"):
        print("Name invalid, must be a txt file.")
        return
    try:
        with open(filename) as file:
            for line in file:
                for char in line:
                    if lowerChar.isalpha():
                        lowerChar = char.lower()
                        chars[lowerChar] = chars[lowerChar] + 1
    except OSError:
        print("Could not open/read file, please check the name inserted.")
        return
    return chars