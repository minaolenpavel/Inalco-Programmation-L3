from employe import Employe

class EmployeTempsPartiel(Employe):
    def __init__(self, nom, age, heures_travaillees:int, taux_horaire:float):
        super().__init__(nom, age)
        if heures_travaillees < 0:
            raise ValueError("Les heures travaillées ne peuvent pas être négatives")
        self.heures_travaillees = heures_travaillees 
        if taux_horaire <= 0:
            raise ValueError("L'esclavage a été interdit en France par décret le 27 avril 1848")
        self.taux_horaire = taux_horaire

    def calcul_salaire(self) -> float:
        return self.heures_travaillees * self.taux_horaire
    
if __name__ == "__main__":
    e1 = EmployeTempsPartiel("Alice", 25, 20, 15.5)
    e2 = EmployeTempsPartiel("Bob", 30, 35, 12.0)

    print(f"Le salaire de {e1.nom} est de {e1.calcul_salaire()} euros.")
    print(f"Le salaire de {e2.nom} est de {e2.calcul_salaire()} euros.")