'''
class BankovniRacun:
    def __init__(self):
        self.__broj_racuna=""
        self.__ime_vlasnika=""
        self.__stanje=0.0
    def get__broj_racuna(self):
        return self.__broj_racuna
    def set__broj_racuna(self):
        self.__broj_racuna='00000'
    def get__ime_vlasnika(self):
        return self.__ime_vlasnika
    def set__ime_vlasnika(self,ime):
        self.__ime_vlasnika=ime
    def get__stanje(self):
        return self.__stanje
    def set__stanje(self, s):
        if s<0:
            self.__stanje=0
        else:
            self.__stanje=s
    def uplati(self,uplata):
        self.__stanje+=uplata
    def podigni(self,suma):
        if self.__stanje<suma:
            print("Nemate dovoljno sredstava")
        else:
            self.__stanje-=suma
            print(f"Podigli ste {suma} , vase novo stanje je {self.__stanje}")
    def prikaz_stanja(self):
        return self.__stanje
racun1=BankovniRacun()
racun1.uplati(190)
print(racun1.prikaz_stanja())
racun1.uplati(150)
print(racun1.prikaz_stanja())
racun1.podigni(240)
print(racun1.prikaz_stanja())
'''
''''
class Knjiga :
    def __init__(self, naziv, autor, godina_izdavanja,broj_stranica,trenutna_stranica):
        self.__naziv=naziv
        self.__autor=autor
        self.__godina_izdavanja=godina_izdavanja
        self.__broj_stranica=broj_stranica
        self.__trenutna_stranica=trenutna_stranica
    def get__naziv(self):
        return self.__naziv
    def set__naziv(self,naziv):
        self.__naziv=naziv
    def get__autor(self):
        return self.__autor
    def set__autor(self,autor):
        self.__autor=autor
    def get__godina_izdavanja(self):
        return self.__godina_izdavanja
    def set__godina_izdavanja(self,godina):
        if godina<2026:
            self.__godina_izdavanja=godina
        else:
            print("Ne moze biti u buducnosti")
    def get__broj_stranica(self):
        return self.__broj_stranica
    def set__broj_stranica(self,stranica):
        if stranica>0:
            self.__broj_stranica=stranica
        else:
            print("Ne moze biti negativan broj")
    def get__trenutna_stranica(self):
        return self.__trenutna_stranica
    def set__trenutna_stranica(self,trstr):
        if trstr>0 and self.__broj_stranica>=trstr:
            self.__trenutna_stranica=trstr
        else:
            self.__trenutna_stranica==1
    def idi_na_stranicu(self, stranica):
        if stranica<=self.__broj_stranica and stranica>0:
            self.__trenutna_stranica=stranica
        else:
            print("Premasili ste broj stranica knjige")
    def sledeca_stranica(self):
        if self.__trenutna_stranica>0 and self.__trenutna_stranica<self.__broj_stranica:
            self.__trenutna_stranica+=1
        else:
            print("Izvan opsega knjige ste")
    def prethodna_stranica(self):
        if self.__trenutna_stranica>1:
            self.__trenutna_stranica-=1
        else:
            print("Ne moze ispod jedan")
    
knjiga1=Knjiga("Dnevnik genija","Salvador Dali",2024,250,250)
knjiga1.sledeca_stranica()   
print(knjiga1.get__trenutna_stranica())
'''

    
