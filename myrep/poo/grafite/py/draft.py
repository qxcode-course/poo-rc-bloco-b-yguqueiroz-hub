import sys

class Lead:

    def __init__(self, thickness: float, hardness: str, size: int):
        self.__thickness = thickness
        self.__hardness = hardness
        self.__size = size


    def get_thickness(self) -> float:
        return self.__thickness 

    def get_hardness(self) -> str:
        return self.__hardness

    def get_size(self) -> int:
        return self.__size

    def set_size(self, new_size: int):
        self.__size = new_size

    def usagePerSheet(self) -> int:
        if self.__hardness == "HB":
            return 1
        elif self.__hardness == "2B":
            return 2
        elif self.__hardness == "4B":
            return 4
        elif self.__hardness == "6B":
            return 6
        return 0
    
    def __str__(self) -> str:
        return f"[{self.__thickness}:{self.__hardness}:{self.__size}]"
    

class Pencil:

    def __init__(self, thickness: float):
        self.__thickness = thickness
        self.__tip = None

    def hasGrafite(self) -> bool:
        return self.__tip is not None
    
    def insert(self, lead: Lead):
        if self.hasGrafite():
            print("fail: ja existe grafite")
            return 
        
        if lead.get_thickness() != self.__thickness:
            print("fail: calibre incompativel")
            return 
        self.__tip = lead

    def remove(self) -> Lead | None:
        if not self.hasGrafite():
            print("fail: nao existe grafit")
            return None
        
        removed_lead = self.__tip
        self.__tip = None
        return removed_lead
    
    def writePage(self):
        if not self.hasGrafite():
            print("fail: nao existe grafite")
            return
        
        current_size = self.__tip.get_size()

        if current_size <= 10:
            print("fail: tamanho insuficiente")
            return 
        usage = self.__tip.usagePerSheet()
        remaining_size = current_size - usage
        if remaining_size < 10:
            self.__tip.set_size(10)
            print("fail: folha incompleta")
        else:
            self.__tip.set_size(remaining_size)
    def __str__(self) -> str:
        calibre_str = f"{self.__thickness:.1f}"
        tip_str = str(self.__tip) if self.hasGrafite() else "null"
        return f"calibre: {calibre_str}, grafite: {tip_str}"
    

def main():

    pencil = None

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
            elif cmd == "init":
                pencil = Pencil(float(parts[1]))

            elif cmd == "show":
                if pencil:
                    print(pencil)
            elif cmd == "insert":
                if pencil:
                    lead = Lead(float(parts[1]), parts[2], int(parts[3]))
                    pencil.insert(lead)
                else:
                    print("fail: lapiseira nao iniciada")
            elif cmd == "remove":
                if pencil:
                    pencil.remove()
                else:
                    print("fail: lapiseira nao iniciada")
            elif cmd == "write":
                if pencil:
                    pencil.writePage()
                else:
                    print("fail: lapiseira nao iniciada")
            elif cmd.startswith("#"):
                pass
            else:
                print("fail: unknown command")
        except EOFError:
            break
        except Exception as e:
            print(f"an error occurred: {e}")
            break
if __name__ == "__main__":
    main()
            