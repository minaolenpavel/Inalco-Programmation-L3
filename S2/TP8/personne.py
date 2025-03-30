class Personne:
    population:int = 0
    individus:list = []
    def __init__(self, nom:str, age:int):
        self.nom:str = nom
        self.age:int = age
        Personne.population +=1
        Personne.individus.append(self)
        if Personne.est_majeur(self.age):
            print(f"{self.nom} est majeur(e)")

    @classmethod
    def nombre_personnes(cls) -> int:
        return cls.population
    
    @classmethod
    def tour_de_table(cls):
        for p in cls.individus:
            p.se_presenter()

    @classmethod
    def est_majeur(cls, age:int) -> bool:
        if age >= 18:
            return True
        else:
            return False

    def se_presenter(self):
        print(f"Je m'appelle {self.nom} et j'ai {self.age} ans.")



if __name__ == "__main__":
    print(Personne.nombre_personnes())
    p1 = Personne("Alice", 25)
    p2 = Personne("Bob", 16)
    print(Personne.nombre_personnes())
    Personne.tour_de_table()