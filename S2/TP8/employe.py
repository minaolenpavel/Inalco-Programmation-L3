from personne import Personne

class Employe(Personne):
    salaire_base:int = 1500
    def __init__(self, nom, age):
        super().__init__(nom, age)

    @classmethod
    def modifier_salaire(cls, nouveau_salaire:int):
        cls.salaire_base = nouveau_salaire

    @staticmethod
    def impots(salaire:int) -> float:
        return salaire * 0.30 



if __name__ =="__main__":
    emp = Employe("Bob", 25)
    Employe.tour_de_table()
    print(Employe.salaire_base) # 1500
    Employe.modifier_salaire(2000)
    print(Employe.salaire_base) # 2000
    print(Employe.impots(2000)) # 600.0 (30% de 2000)