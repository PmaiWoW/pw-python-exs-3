class Automovel():
    def __init__ (self, cap_dep, quant_comb, consumo):
        self.cap_dep = cap_dep
        self.quant_comb = quant_comb
        self.consumo = consumo
        
    def Combustivel(self):
        return self.quant_comb
    
    def Autonomia(self):
        autonomia = self.quant_comb/self.consumo * 100
        return int(autonomia)
    
    def Abastece(self, litros):
        newQuantity = self.quant_comb + litros
        if newQuantity > self.cap_dep:
            print("Abastecimento excederia capacidade máxima. Abortado.")
            return
        quant_comb = newQuantity
        return quant_comb
    
    def Percorre(self, kms):
        distMax = self.Autonomia()
        if kms > distMax:
            print("Combustível insuficiente para percorrer esta distância. Abortado.")
            return
        litersUsed = kms * (self.consumo/100)
        self.quant_comb -= int(litersUsed)
        return int(self.Autonomia())