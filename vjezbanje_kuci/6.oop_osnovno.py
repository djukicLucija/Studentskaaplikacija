#1.zadatak 
'''
class Televizor:
    def __init__(self):
        self.__broj_tekuceg_kanala=0
        self.__naziv_tekuceg_kanala=""
        self.__kanali=[]
        self.__jacina_tona=0
    def get_broj_tekuceg_kanala(self):
        return self.__broj_tekuceg_kanala
    def set_broj_tekuceg_kanala(self,broj):
        if 0 <= broj < len(self.__kanali):
            self.__broj_tekuceg_kanala=broj
            self.__naziv_tekuceg_kanala=self.__kanali[broj]
        else:
            print("Nevalidan broj kanala")
    def get_naziv_tekudjeg_kanala(self):
        return self.__naziv_tekuceg_kanala
    def get_kanali(self):
        return self.__kanali
    def get_jacina_tona(self):
        return self.__jacina_tona
    def set_jacina_tona(self,jacina):
        if 0 <=jacina<=10:
            self.__jacina_tona=jacina
        else:
            print("Nevalidna jacina, mora biti izmedju 0 i 10")
    def dodaj_kanal(self,naziv_kanala):
        self.__kanali.append(naziv_kanala)
    def obrisi_kanal(self,naziv_kanala):
        if naziv_kanala in self.__kanali:
            self.__kanali.remove(naziv_kanala)
            if self.__naziv_tekuceg_kanala ==naziv_kanala:
                self.__naziv_tekuceg_kanala=""
                self.__broj_tekuceg_kanala=0
        else:
            print("Kanal ne postoji")
    def pojacaj_ton(self):
        self.set_jacina_tona(self.__jacina_tona + 1)

    def ime_kanala(self,broj_kanala):
        if 1<=broj_kanala<=len(self.__kanali):
            return self.__kanali[broj_kanala-1]
        else:
            print("Nepostojeci broj kanala")

tv = Televizor()

tv.dodaj_kanal("Pink")
tv.dodaj_kanal("TV E")
tv.dodaj_kanal("RTCG")
print(tv.get_kanali())

tv.obrisi_kanal("Pink")
print(tv.get_kanali())

tv.set_broj_tekuceg_kanala(1)
print(tv.get_naziv_tekudjeg_kanala())

tv.set_jacina_tona(5)
tv.pojacaj_ton()
print(tv.get_jacina_tona())
'''
#2 Knjiga
"""class Knjiga:
    def __init__(self, naziv, autor, godina_izdavanja, broj_stranica):
        self.__naziv = naziv
        self.__autor = autor
        self.__godina_izdavanja = godina_izdavanja
        self.__broj_stranica = broj_stranica
        self.__trenutna_stranica = 1

    def get_naziv(self):
        return self.__naziv

    def set_naziv(self, naziv):
        self.__naziv = naziv

    def get_autor(self):
        return self.__autor

    def set_autor(self, autor):
        self.__autor = autor

    def get_godina_izdavanja(self):
        return self.__godina_izdavanja

    def set_godina_izdavanja(self, godina):
        if godina <= 2025:
            self.__godina_izdavanja = godina
        else:
            print("Godina izdavanja ne može biti u budućnosti.")

    def get_broj_stranica(self):
        return self.__broj_stranica

    def set_broj_stranica(self, broj):
        if broj > 0:
            self.__broj_stranica = broj
        else:
            print("Broj stranica mora biti pozitivan broj.")

    def get_trenutna_stranica(self):
        return self.__trenutna_stranica

    def idi_na_stranicu(self, broj_stranice):
        if 1 <= broj_stranice <= self.__broj_stranica:
            self.__trenutna_stranica = broj_stranice
        else:
            print("Stranica je van opsega.")

    def sledeca_stranica(self):
        if self.__trenutna_stranica < self.__broj_stranica:
            self.__trenutna_stranica += 1
        else:
            print("Već ste na poslednjoj stranici.")

    def prethodna_stranica(self):
        if self.__trenutna_stranica > 1:
            self.__trenutna_stranica -= 1
        else:
            print("Već ste na prvoj stranici.")

# Primer korišćenja:
knjiga = Knjiga("Na Drini Ćuprija", "Ivo Andrić", 1945, 350)

print(knjiga.get_naziv())
print(knjiga.get_autor())
print(knjiga.get_godina_izdavanja())

knjiga.idi_na_stranicu(100)
print(knjiga.get_trenutna_stranica())

knjiga.sledeca_stranica()
print(knjiga.get_trenutna_stranica())

knjiga.prethodna_stranica()
print(knjiga.get_trenutna_stranica())"""

#3 Student 
"""class Student:
    def __init__(self, ime, prezime, broj_indeksa):
        self.__ime = ime
        self.__prezime = prezime
        self.__broj_indeksa = broj_indeksa
        self.__polozeni_ispiti = []

    def get_ime(self):
        return self.__ime

    def set_ime(self, ime):
        self.__ime = ime

    def get_prezime(self):
        return self.__prezime

    def set_prezime(self, prezime):
        self.__prezime = prezime

    def get_broj_indeksa(self):
        return self.__broj_indeksa

    def set_broj_indeksa(self, broj_indeksa):
        if broj_indeksa:
            self.__broj_indeksa = broj_indeksa
        else:
            print("Broj indeksa ne može biti prazan.")

    def get_polozeni_ispiti(self):
        return self.__polozeni_ispiti

    def dodaj_ispit(self, predmet):
        if predmet not in self.__polozeni_ispiti:
            self.__polozeni_ispiti.append(predmet)
        else:
            print("Ispit već postoji u listi položenih ispita.")

    def ukloni_ispit(self, predmet):
        if predmet in self.__polozeni_ispiti:
            self.__polozeni_ispiti.remove(predmet)
        else:
            print("Ispit nije pronađen u listi.")

    def broj_polozenih(self):
        return len(self.__polozeni_ispiti)

# Primer korišćenja:
student = Student("Marko", "Marković", "2023/0123")

student.dodaj_ispit("Matematika")
student.dodaj_ispit("Programiranje")

print(student.get_polozeni_ispiti())
print(student.broj_polozenih())

student.ukloni_ispit("Matematika")
print(student.get_polozeni_ispiti())
print(student.broj_polozenih())"""

#4 Bankovni racun
"""class BankovniRacun:
    def __init__(self, broj_racuna, ime_vlasnika):
        self.__broj_racuna = broj_racuna
        self.__ime_vlasnika = ime_vlasnika
        self.__stanje = 0.0

    def get_broj_racuna(self):
        return self.__broj_racuna

    def set_broj_racuna(self, broj_racuna):
        self.__broj_racuna = broj_racuna

    def get_ime_vlasnika(self):
        return self.__ime_vlasnika

    def set_ime_vlasnika(self, ime_vlasnika):
        self.__ime_vlasnika = ime_vlasnika

    def get_stanje(self):
        return self.__stanje

    def set_stanje(self, stanje):
        if stanje >= 0:
            self.__stanje = stanje
        else:
            print("Stanje ne sme biti negativno.")

    def uplati(self, iznos):
        if iznos > 0:
            self.__stanje += iznos
        else:
            print("Iznos za uplatu mora biti pozitivan.")

    def podigni(self, iznos):
        if 0 < iznos <= self.__stanje:
            self.__stanje -= iznos
        else:
            print("Nedovoljno sredstava na računu ili neispravan iznos.")

    def prikazi_stanje(self):
        return self.__stanje

# Primer korišćenja:
racun = BankovniRacun("123456789", "Petar Petrović")

racun.uplati(1500)
print(racun.prikazi_stanje())

racun.podigni(500)
print(racun.prikazi_stanje())

racun.podigni(2000)  # Primer neuspešnog podizanja zbog nedovoljno sredstava"""
#5 Vozilo i naslijedjena
'''
class Vozilo:
    def __init__(self, registracija, marka, model, godina, predjeno_km):
        self.registracija = registracija
        self.marka = marka
        self.model = model
        self.godina = godina
        self.predjeno_km = predjeno_km
        self.dostupno = True

    def iznajmi(self):
        if self.dostupno:
            self.dostupno = False
            return f"Vozilo {self.registracija} uspješno iznajmljeno."
        else:
            return f"Greška: Vozilo {self.registracija} već je iznajmljeno!"

    def vrati(self, km):
        self.predjeno_km += km
        self.dostupno = True
        return f"Vozilo {self.registracija} je vraćeno. Trenutna kilometraža: {self.predjeno_km} km."

    def status(self):
        stanje = "dostupno" if self.dostupno else "iznajmljeno"
        return f"Vozilo {self.registracija}: {stanje}, pređeno {self.predjeno_km} km."

    def __str__(self):
        return f"{self.marka} {self.model} ({self.godina}), Reg: {self.registracija}"

class ElektricniAutomobil(Vozilo):
    def __init__(self, registracija, marka, model, godina, predjeno_km, kapacitet_baterije, napunjenost_baterije):
        super().__init__(registracija, marka, model, godina, predjeno_km)
        self.kapacitet_baterije = kapacitet_baterije
        self.napunjenost_baterije = napunjenost_baterije

    def iznajmi(self):
        if self.napunjenost_baterije >= 20:
            return super().iznajmi()
        else:
            return "Greška: Baterija nije dovoljno napunjena za iznajmljivanje!"

    def napuni_bateriju(self):
        self.napunjenost_baterije = 100
        return "Baterija je potpuno napunjena."

    def __str__(self):
        osnovno = super().__str__()
        return f"{osnovno}, baterija: {self.napunjenost_baterije}% ({self.kapacitet_baterije} kWh)"

class SportskiAutomobil(Vozilo):
    def __init__(self, registracija, marka, model, godina, predjeno_km, maksimalna_brzina, stanje_guma):
        super().__init__(registracija, marka, model, godina, predjeno_km)
        self.maksimalna_brzina = maksimalna_brzina
        self.stanje_guma = stanje_guma

    def iznajmi(self):
        if self.stanje_guma != "Loše":
            return super().iznajmi()
        else:
            return "Greška: Gume su u lošem stanju! Zamijenite ih prije iznajmljivanja."

    def zamijeni_gume(self):
        self.stanje_guma = "Novo"
        return "Gume su zamijenjene novim."

    def izvedi_drift(self):
        if self.stanje_guma == "Novo":
            self.stanje_guma = "Dobro"
            return "Drift izveden, gume sada u dobrom stanju."
        elif self.stanje_guma == "Dobro":
            self.stanje_guma = "Loše"
            return "Drift izveden, gume sada u lošem stanju."
        else:
            return "Greška: Gume su loše, nije sigurno driftovati!"

    def __str__(self):
        osnovno = super().__str__()
        return f"{osnovno}, max brzina: {self.maksimalna_brzina} km/h, stanje guma: {self.stanje_guma}"


vozilo = Vozilo("PG-AB123", "Volkswagen", "Golf", 2020, 45000)
el_auto = ElektricniAutomobil("PG-EL001", "Tesla", "Model 3", 2022, 15000, 75, 15)
sport_auto = SportskiAutomobil("PG-SP777", "BMW", "M3", 2021, 22000, 280, "Dobro")

print(vozilo.status())
print(el_auto.iznajmi())  # Neće moći zbog baterije
print(el_auto.napuni_bateriju())
print(el_auto.iznajmi())
print(sport_auto.iznajmi())
print(sport_auto.izvedi_drift())
print(sport_auto.zamijeni_gume())
print(sport_auto.izvedi_drift())
print(sport_auto.izvedi_drift()) 
print(sport_auto)
'''
