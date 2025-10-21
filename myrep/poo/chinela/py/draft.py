class Chinela: 
    def __init__(self):
        self.__tamanho = 0

    def getTamanho(self):
        return self.__tamanho
    
    def setTamanho(self, valor: int):
        if valor < 20 or valor > 50:
            print("Erro: o tamanho deve estar entre 20 e 50")
        elif valor % 2 != 0:
            print("Erro: o tamanho deve ser um número par.")
        else:
            self.__tamanho = valor
            print("Tamanho registrado com sucesso")

chinela = Chinela()

while chinela.getTamanho() == 0:
    print("Digite o tamanho da sua chinela")
    tamanho = int(input())
    chinela.setTamanho(tamanho)

print ("Parabéns você acabou de comprar uma chinela tamanho", chinela.getTamanho())