import analisa_total_pasta

def main():
    folder = analisa_total_pasta.pede_pasta()
    sum = analisa_total_pasta.calcula_tamanho_pasta(folder)
    print("Tamanho total da pasta: " + str(sum) + " MB")
    
if __name__ == "__main__":
    main()