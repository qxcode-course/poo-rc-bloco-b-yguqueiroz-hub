import sys

class Pessoa:
    def __init__(self, nome: str, dinheiro: float):
        self.__nome = nome
        self.__dinheiro = float(dinheiro)

    def get_nome(self) -> str:
        return self.__nome
    
    def get_dinheiro(self) -> float:
        return self.__dinheiro
    
    def receber(self, valor:float):
        self.__dinheiro += valor

    def pagar(self, valor: float) -> float:
        if self.__dinheiro >= valor:
            self.__dinheiro -= valor
            return valor
        else:
            valor_pago = self.__dinheiro
            self.__dinheiro = 0.0
            return valor_pago


    def __str__(self) -> str:
        return f"{self.__nome}:{self.__dinheiro:.0f}"
    
class Moto:
    def __init__(self):
        self.__custo = 0.0
        self.__motorista = None
        self.__passageiro = None

    def setDriver(self, nome: str, dinheiro: float):
        self.__motorista = Pessoa(nome, dinheiro)

    def setPass(self,nome: str, dinheiro:float):
        if self.__motorista is None:
            print("fail: no driver")
            return
        if self.__passageiro is not None:
            print("fail: passenger already on the bike")
            return
        self.__passageiro = Pessoa(nome, dinheiro)

    def drive(self, km: float):
        if self.__motorista is None:
            print("fail: no driver")
            return
        if self.__passageiro is None:
            print("fail: no passenger to drive")
            return
        self.__custo += float(km) * 1


    def leavePass(self):
        if self.__passageiro is None:
            print("fail: no passenger to leave")
            return
        
        custo_total = self.__custo
        
        if self.__passageiro.get_dinheiro() < custo_total:
            print("fail: Passenger does not have enough money")

        self.__passageiro.pagar(custo_total)

        self.__motorista.receber(custo_total)

        print(f"{self.__passageiro.get_nome()}:{self.__passageiro.get_dinheiro():.0f} left")
        self.__passageiro = None
        self.__custo = 0.0

    def __str__(self) -> str:
        driver_str = str(self.__motorista) if self.__motorista else "None"
        pass_str = str(self.__passageiro) if self.__passageiro else "None"

        return f"Cost: {self.__custo:.0f}, Driver: {driver_str}, Passenger: {pass_str}"


def main():

    moto = Moto()

    sys.stdin.reconfigure(encoding='utf-8')
    sys.stdout.reconfigure(encoding='utf-8')

    while True:
        try:
            line = input()
            if line.strip() == "":
                continue
            print(f"${line}")
            parts = line.split()
            cmd = parts[0]
            
            if cmd == "end":
                break
            elif cmd == "show":
                print(moto)
            elif cmd == "setDriver":
                moto.setDriver(parts[1], float(parts[2]))
            elif cmd == "setPass":
                moto.setPass(parts[1], float(parts[2]))
            elif cmd =="drive":
                moto.drive(float(parts[1]))
            elif cmd == "leavePass":
                moto.leavePass()
            elif cmd.startswith("#"):
                pass
            else:
                print("fail: unknown command")
        except EOFError:
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break
if __name__ == "__main__":
    main()