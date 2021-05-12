import analise_pasta
   
def main():
    print("\nEste programa analisa os tipos e tamanhos de ficheiros na pasta que indicar.")
    path = analise_pasta.pede_pasta()
    filesInfoDict = analise_pasta.faz_calculos(path)
    analise_pasta.guarda_resultados(filesInfoDict)

    filesInfoKeys = list(filesInfoDict.keys())
    filesInfoVals = list(filesInfoDict.values())

    quantityList = []
    volumesList = []

    for val in filesInfoVals:
        quantityList.append(val["Quantidade"])
    for val in filesInfoVals:
        volumesList.append(val["Volume(kB)"])

    #pie chart for quantities
    analise_pasta.faz_grafico_queijos("Quantidade", filesInfoKeys, quantityList)
    #pie chart for volumes
    analise_pasta.faz_grafico_queijos("Volume(kB)", filesInfoKeys, volumesList)

    #pie chart for quantities
    analise_pasta.faz_grafico_barras("Quantidade", filesInfoKeys, quantityList)
    #pie chart for volumes
    analise_pasta.faz_grafico_barras("Volume(kB)", filesInfoKeys, volumesList)
    return

if __name__ == "__main__":
    main()