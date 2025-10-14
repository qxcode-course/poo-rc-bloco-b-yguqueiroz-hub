class Pessoa:
    def __init(self, nome: str):
        self.nome = nome

    def __str__(self)
class moto:
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

def main():

    moto = Moto()
