'''
class Vozilo:
    def __init__(self, registracija, marka, model, godina, predjeno_km):
        self.registracija=registracija
        self.marka=marka
        self.model=model
        self.godina=godina
        self.predjeno_km=predjeno_km
        self.dostupno=True
    def iznajmi(self):
        if self.dostupno:
            self.dostupno=False
            return f"Vozilo {self.registracija} je uspjesno iznajmljeno"
        else:
            return f"Greska:Vozilo{self.registracija} je vec iznajmljeno"
    def vrati(self,kilometri):
        self.predjeno_km+=kilometri
        self.dostupno=True
        return f"Vozilo{self.registracija} je vraceno. Trenutna kilometraza je {self.predjeno_km}"
    def status(self):
        stanje="dostupno" if self.dostupno else "iznajmljeno"
        return f"Vozilo {self.registracija} je {stanje}, preslo je {self.predjeno_km}"
    def __str__(self):
        return f"{self.marka},{self.model},({self.godina}), Reg:{self.registracija}"        
class ElektricniAutomobil(Vozilo):
    def __init__(self, registracija, marka, model, godina, predjeno_km, kapacitet_baterije,napunjenost_baterije):
        super().__init__(registracija, marka, model, godina, predjeno_km)
        self.kapacitet_baterije=kapacitet_baterije
        self.napunjenost_baterije=napunjenost_baterije
    def iznajmi(self):
        if self.napunjenost_baterije>=20:
            return super().iznajmi()
        else:
            return "Greska, baterija nije napunjena"
    def napuni_bateriju(self):
        self.napunjenost_baterije=100
        return "Baterija je napunjena"
    def __str__(self):
        osnova= super().__str__()
        return f"{osnova},baterija:{self.napunjenost_baterije}%, a kapacitet je{self.kapacitet_baterije} kWh"
class SportskiAutomobil(Vozilo):
    def __init__(self, registracija, marka, model, godina, predjeno_km, maksimalna_brzina, stanje_guma):
        super().__init__(registracija, marka, model, godina, predjeno_km)
        self.maksimalna_brzina=maksimalna_brzina
        self.stanje_guma=stanje_guma
    def iznajmi(self):
        if self.stanje_guma !="Lose":
            return super().iznajmi()
        else:
            return "Greska, gume su u losem stanju. Zamjenite ih."
    def zamjeni_gume(self):
        self.stanje_guma="Novo"
        return "Gume su zamjenjene"
    def izvedi_drift(self):
        if self.stanje_guma=="Novo":
            self.stanje_guma="Dobro"
            return "Drift uspjesan, gume su sada u dobrom stanju"
        elif self.stanje_guma=="Dobro":
            self.stanje_guma="Lose"
            return "Drift je uspjesan, gume su sada u losem stanju"
        else:
            return "Drift neuspjesan, gume su lose, zamjenite ih"
    def __str__(self):
        osnovno= super().__str__()
        return f'{osnovno}, maksimalna brzina je: {self.maksimalna_brzina} km/h, a stanje guma je{self.stanje_guma}'
vozilo=Vozilo("NK-CT212","Volksvagen","Golf",2020,145000)
el_auto=ElektricniAutomobil("PG-EL101","Tesla","Model 3", 2022,15000,75,15)
sport_auto=SportskiAutomobil("BA=AG111","BMW","M3",2021,240000,240,"Dobro")
'''print(vozilo.status())'''
print(el_auto.iznajmi())
print(el_auto.napuni_bateriju())
print(el_auto.iznajmi())
print(sport_auto.iznajmi())
print(sport_auto.izvedi_drift())
print(sport_auto.izvedi_drift())
print(sport_auto.iznajmi())
print(sport_auto.zamjeni_gume())
print(sport_auto.izvedi_drift())
print(sport_auto.izvedi_drift())
print(vozilo)
print(el_auto)
print(sport_auto)
'''