class Camisa:
    
    TAMANHOS_VALIDOS  = ("PP" , "P", "M", "G", "GG" , "XG")

    def __init__(self):
        self.__tamanho: str = ""

    def getTamanho(self) -> str:
        return self.__tamanho

    def setTamanho(self, valor: str):
        if valor is None:
            valor = ""
        valor_normalizado = valor.strip().upper()
        if valor_normalizado in Camisa.TAMANHOS_VALIDOS:
            self.__tamanho = valor_normalizado
        else:
            permitidos = ", ".join(Camisa.TAMANHOS_VALIDOS)
            print (f" Erro: tamanho inválido ' {valor}'. valores permitidos: {self.TAMANHOS_VALIDOS}")


def main():
    roupa = Camisa()
    while roupa.getTamanho() == "":
        try:
            resposta = input("Digite seu tamanho de roupa (PP, P, M, G, GG, XG):")
        except EOFError:
            print("\nErro de entrada: Não foi possivel ler mais dados. encerrando programa.")
            return 
        roupa.setTamanho(resposta)
        
    print("Parabéns, você comprou uma roupa tamanho", roupa.getTamanho())
    

    
if __name__ == "__main__":
    main()