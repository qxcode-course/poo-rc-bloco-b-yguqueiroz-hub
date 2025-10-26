class Camisa:
    
    TAMANHOS_VALIDOS  = ("PP" , "P", "M", "G", "GG" , "XG")

    def __init__(self):
        self.__tamanho = ""
    
    @property
    def tamanho(self) -> str:
      return self.__tamanho
    
    @tamanho.setter
    def tamanho(self, valor: str):
        if valor is None:
            valor = ""
        valor_normalizado = valor.strip().upper()
        if valor_normalizado in Camisa.TAMANHOS_VALIDOS:
            self.__tamanho = valor_normalizado
        else:
            pass


def main():
    roupa = Camisa()
    while True:
        try:
            resposta = input().strip()
            print(f"${resposta}")
        except EOFError:
            break
        
        cmd = resposta.lower()

        if cmd == "show":
            print(f"size: ({roupa.tamanho})")
            continue

        if cmd == "end":
            break

        if cmd.startswith("size "):
            valor = resposta[len("size "):]
            valor = valor.strip()

            tamanho_antigo = roupa.tamanho
            roupa.tamanho = valor

            if roupa.tamanho == tamanho_antigo and valor.strip().upper() not in Camisa.TAMANHOS_VALIDOS:
                print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
            else: 
                pass
            continue

        else:
            print("Fail: comando inválido")
    
if __name__ == "__main__":
     main()