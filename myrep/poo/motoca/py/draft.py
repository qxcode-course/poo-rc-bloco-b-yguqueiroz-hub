class Pessoa:
    def __init(self, nome: str, idade: int):
        self.__nome = nome
        self.__idade = idade

    def getName(self):
        return self.__nome
    def getAge(self):
        return self.__idade
    def toString(self):
        return f"{self.__nome}:{self.__idade}"

        
class Moto:

    def __init__(self):
        self.pessoa: Pessoa | None = None

    def inserir(self, pessoa : Pessoa) -> bool:
        if self.pessoa != None:
            print("ja tem gente na moto")
            return True
        self.pessoa = pessoa
        return False

    def remover(self) -> Pessoa | None:
        aux = self.pessoa
        self.pessoa = None
        return aux
    
    def comprarTempo(self, time: int):
        self.time =+ time


    def dirigir(self, time_drive: int):
        if self.time == 0>
        print("compre tempo")
        return
        if self.pessoa is None:
            print("motoca vazia")
            return
        if self.pessoa.getAge() > 10:
            print("muito velho para dirigir")
            return
        
        tempo_restante = self.time - time_drive
        if tempo_restante < 0:
            print("acabou o tempo {self.time} minutes")
            self.time = 0
            return
        self.time = tempo_restante

        def honk(self) -> str:
            return "p" + "e" * self.potencia + "m"
        def __str__(self): 
            pessoa_str = self.pessoa.toString() if self.pessoa else "vazio"
            return f"power:{self.potencia}, time:{self.time}, person:({pessoa_str})"