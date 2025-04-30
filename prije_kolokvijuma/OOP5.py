'''
#Zadatak 1
class Televizor:
    def __init__(self):
        self.__broj_tekuceg_kanala=0
        self.__naziv_tekuceg_kanala=""
        self.__kanali=[]
        self.__jacina_tona=0
    def get_broj_tekuceg_kanala(self):
            return self.__broj_tekuceg_kanala
    def set_broj_tekuceg_kanala(self,broj):
            if 0<=broj < len(self.__kanali):
                self.__broj_tekuceg_kanala=broj
                self.__naziv_tekuceg_kanala=self.__kanali[broj]
            else:
                print("Nevalidan broj kanala")
    def get_naziv_tekuceg_kanala(self):
         return self.__naziv_tekuceg_kanala
    def get_kanali(self):
        return self.__kanali
    def get_jacina_tona(self):
        return self.__jacina_tona
    def set_jacina_tona(self,jacina):
        if 0<=jacina<=10:
            self.__jacina_tona=jacina
        else:
            print("Nevalidna jacina, mora biti izmedju 0 i 10")
    def dodaj_kanal(self,naziv_kanala):
        self.__kanali.append(naziv_kanala)
    def obrisi_kanal(self,naziv_kanala):
        if naziv_kanala in self.__kanali:
            self.__kanali.remove(naziv_kanala)
            if self.__naziv_tekuceg_kanala==naziv_kanala:
                self.__naziv_tekuceg_kanala=""
                self.__broj_tekuceg_kanala=0
        else:
            print("Kanal ne postoji")
    def pojacaj_ton(self):
        self.set_jacina_tona(self.__jacina_tona+1)

    def ime_kanala(self,broj_kanala):
        if 1<=broj_kanala<=len(self.__kanali):
            return self.__kanali[broj_kanala-1]
        else:
            print("Nepostojeci broj kanala")

tv=Televizor()
tv.dodaj_kanal("Pink")
tv.dodaj_kanal("TV E")
tv.dodaj_kanal("RTCG")
print(tv.get_kanali())
tv.obrisi_kanal("Pink")
print(tv.get_kanali())

tv.set_broj_tekuceg_kanala(1)
print(tv.get_naziv_tekuceg_kanala())
tv.set_jacina_tona(5)
tv.pojacaj_ton()
print(tv.get_jacina_tona())
'''
#Zadatak 2
'''
class Student:
    def __init__(self, ime, prezime, broj_indeksa,lista_polozenih_ispita):
        self.__ime=ime
        self.__prezime=prezime
        self.__broj_indeksa=broj_indeksa
        self.__lista_polozenih_ispita=lista_polozenih_ispita
    def get__ime(self):
        return self.__ime
    def set__ime(self,ime):
        self.__ime=ime
    def get__prezime(self):
        return self.__prezime
    def set__prezime(self,prezime):
        self.__prezime=prezime
    def get__broj_indeksa(self):
        return self.__broj_indeksa
    def set__broj_indeksa(self,broj_indeksa):
        if broj_indeksa !=0:
            self.__broj_indeksa=broj_indeksa
        else:
            print("Unijeli ste pogresan broj indeksa")
    def get__lista_polozenih_ispita(self):
        return self.__lista_polozenih_ispita
    def set__lista_polozenih_ispita(self):
        self.__lista_polozenih_ispita=[]
    def dodaj_ispit(self,naziv):
        if naziv not in self.__lista_polozenih_ispita:
            self.__lista_polozenih_ispita.append(naziv)
        else:
            print("Ispit vec postoji")
    def ukloni_ispit(self, naziv):
        if naziv in self.__lista_polozenih_ispita:
            self.__lista_polozenih_ispita.remove(naziv)
        else:
            print("Predmet ne postoji u listi")
    def broj_polozenih_ispita(self):
        broj=len(self.__lista_polozenih_ispita)
        return(broj)

student1=Student("Marko","Mirkovic","22/023",["Matematika","Maternji","Biologija"])
student2=Student("Milija","Milic","22/015", ["Engleski","Marketing","Spanski"])    
student1.dodaj_ispit("Statistika")
print(student1.get__lista_polozenih_ispita())
'''
    
        

