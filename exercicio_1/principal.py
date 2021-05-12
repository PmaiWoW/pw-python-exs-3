import os
import json
import analisa_ficheiro

def main():
    print("\nNº de linhas: " + str(analisa_ficheiro.calculos.calcula_linhas("pessoa.json")))
    print("\nNº de chars: " + str(analisa_ficheiro.calculos.calcula_carateres("pessoa.json")))
    print("\nPalavra mais longa: " + analisa_ficheiro.calculos.calcula_palavra_comprida("pessoa.json"))
    print("\Dictionary de chars e nº deles: " + str(analisa_ficheiro.calculos.calcula_ocorrencia_de_letras("pessoa.json")))
    print("\nNome do txt file: " + analisa_ficheiro.acessorio.pede_nome("test.txt"))
    print("\nNome do json file (ver ficheiro test.json para output do ficheiro test.txt): " + str(analisa_ficheiro.acessorio.gera_nome("test.txt")))
    return

if __name__ == "__main__":
    main()