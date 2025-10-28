import sys

class Charger:
    def __init__(self, potencia: int):
        self.__potencia = potencia

    def get_potencia(self) -> int:
        return self.__potencia
    def __str__(self) -> str:
        return f"{self.__potencia}W"
class Battery:
    def __init__(self, capacidade: int):
        self.__capacidade = capacidade
        self.__carga = capacidade

    def get_carga(self) -> int:
        return self.__carga
    def get_capacidade(self) -> int:
        return self.__capacidade
    def carregar(self, tempo: int, potencia: int):
        carga_ganha = tempo * potencia
        self.__carga += carga_ganha
        if self.__carga > self.__capacidade:
            self.__carga = self.__capacidade

    def gastar(self, tempo:int) -> tuple[bool, int]:
        if tempo > self.__carga:
            tempo_gasto = self.__carga
            self.__carga = 0
            return (False, tempo_gasto)
        self.__carga -= tempo
        return (True, tempo)
    def __str__(self) -> str:
        return f"{self.__carga}/{self.__capacidade}"
    
class Notebook:
    def __init__(self):
        self.__ligado = False
        self.__tempo_uso = 0
        self.__carregador = None
        self.__bateria = None

    def set_charger(self, potencia: int):
        if self.__carregador is not None:
            print("fail: carregador já conectado")
            return
        self.__carregador = Charger(potencia)

    def rm_charger(self):
        if self.__carregador is None:
            print("fail: Sem carregador")
            return
        
        removed_str = str(self.__carregador)
        self.__carregador = None
        print(f"Removido {removed_str}")
        self.__check_power_status()

    def set_battery(self, capacidade: int):
        if self.__bateria is not None:
            print("fail: bateria ja conectada")
            return
        self.__bateria = Battery(capacidade)

    def rm_battery(self):
        if self.__bateria is None:
            print("fail: Sem bateria")
            return
        
        removed_str = str(self.__bateria)
        self.__bateria = None
        print(f"Removido {removed_str}")
        self.__check_power_status()

    def __check_power_status(self):

        if not self.__ligado:
            return

        if self.__carregador is not None:
            return
        
        if self.__bateria is not None and self.__bateria.get_carga() > 0:
            self.__ligado = True
            return
        
        print("fail: não foi possivel ligar")
        
    def turn_on(self):
        if self.__ligado:
            return
         

    def use(self, tempo: int):
        if not self.__ligado:
            print("fail: desligado")
            return
        
        if self.__carregador is not None and self.__bateria is None:
            self.__tempo_uso += tempo

        elif self.__carregador is not None and self.__bateria is not None:
            potencia = self.__carregador.get.potencia()
            self.__bateria.carregar(tempo, potencia)
            self.__tempo_uso += tempo

        elif self.__carregador is None and self.__bateria is not None:
            (success, tempo_gasto) = self.__bateria.gastar(tempo)
            self.__tempo_uso += tempo_gasto

            if not success:
                print("fail: descaregou")
                self.__check_power_status()


    def __str__(self) -> str:
        parts = []
        if self.__ligado:
            parts.append(f"ligado por {self.__tempo_uso} min")
        else:
            parts.append("desligado")

        if self.__carregador is not None:
            parts.append(f"Carregador {str(self.__carregador)}")

        if self.__bateria is not None:
            parts.append(f"Bateria {str(self.__bateria)}")
        return "Notebook: " + ", ".join(parts)
    
def main():
    notebook = Notebook()

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
                print(notebook)
            elif cmd == "set_charger":
                notebook.set_charger(int(parts[1]))
            elif cmd == "rm_charger":
                notebook.rm_charger()
            elif cmd == "set_battery":
                notebook.set_battery(int(parts[1]))
            elif cmd == "rm_battery":
                notebook.rm_battery()
            elif cmd == "turn_on":
                notebook.turn_on()
            elif cmd == "use":
                notebook.use(int(parts[1]))
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