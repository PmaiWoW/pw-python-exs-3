import automovel
import os

clear = lambda: os.system('cls')

def main():
    print("Gestor de carro")
    capacity = ""
    quantity = ""
    consumption = ""
    
    while not capacity.isnumeric():
        capacity = input("Insira uma capacidade máxima para o depósito: ")
        if not capacity.isnumeric():
            print("Não é um número inteiro, tente de novo.")
    
    while not quantity.isnumeric():
        quantity = input("Insira a quantidade de combustível inicial: ")
        if not quantity.isnumeric():
            print("Não é um número inteiro, tente de novo.")
            
    while not consumption.isnumeric():
        consumption = input("Insira o valor do consumo (Litros/100KM): ")
        if not consumption.isnumeric():
            print("Não é um número inteiro, tente de novo.")
        
    a1 = automovel.Automovel(int(capacity), int(quantity), int(consumption))

    quit = False

    while quit == False:
        print("\nSelecione uma ação:\n1. Verificar combustível\n2. Verificar autonomia (Kms que pode percorrer)\n3. Abastecer\n4. Percorrer distância\n5. Fechar App\n")
        action = input("")
        
        if action == "1":
            print("Combustível disponível: " + str(a1.Combustivel()))
            
        if action == "2":
            print("Autonomia: " + str(a1.Autonomia()))
            
        if action == "3":
            quant = ""
            
            while not quant.isnumeric():
                quant = input("Insira um quantidade (em Litros) para abastecer: ")
                if not quant.isnumeric():
                    print("Não é um número inteiro, tente de novo.")
            
            print("Nova quantidade de combustível disponível: " + str(a1.Abastece(int(quant))))
        
        if action == "4":
            dist = ""
            
            while not dist.isnumeric():
                dist = input("Distância a percorrer: ")
                if not dist.isnumeric():
                    print("Não é um número inteiro, tente de novo.")
            
            print("Nova autonomia: " + str(a1.Percorre(int(dist))))
            print("Combustível disponível após percorrer distância: " + str(a1.Combustivel()))
        
        if action == "5":
            quit = True

    print("Até à próxima!")
        
if __name__ == "__main__":
    main()
    