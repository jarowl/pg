class Auto:
    def __init__(self, znacka, model):
          self.znacka = znacka
          self.model = model

class Osoba:
    def __init__(self, jmeno, vek):
            self.jmeno = jmeno
            self.vek = vek

    def kup_sproty(self):
          print(f'"Hm, asi si jdu koupit sproty." rekl {self.jmeno} a sel do Kaufu.')

class Zvire:
    def __init__(self, jmeno, druh):
        self.jmeno = jmeno 
        self.druh = druh
        
class Kocka(Zvire):
    def __init__(self, jmeno, druh):
         super().__init__(jmeno, druh)
    def mnoukej(self):
         print(f"{self.jmeno} meows.")

if __name__ == "__main__":
    osoba1 = Osoba("Jakub", 69)
    osoba1.kup_sproty()

    kock = Kocka("Diddy", "cerna kocka")
    kock.mnoukej()