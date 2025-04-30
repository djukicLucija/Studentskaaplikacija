
#1.Zadatak 
'''
studenti=[{"ime":"marko","prosjek":8.5,"godina":2,"aktivan":"Da",'smjer':'psihologija'},
          {"ime":"jovan","prosjek":9.5,"godina":1,"aktivan":"Da",'smjer':'dizajn'},
          {"ime":"marko","prosjek":10.,"godina":3,"aktivan":"Da",'smjer':"razunarstvo"}]
def broj_aktivnih_studenata(s):
    broj=0
    for student in s:
        if student["aktivan"]:
            broj+=1
    return(broj)
def najbolji_student(s):
    najbolji_student1=''
    prosjek_najb=0.0
    for student in s:
        if student["prosjek"]>prosjek_najb:
            prosjek_najb=student["projek"]
            najbolji_student=student["ime"]
    return(f"Najbolji student je {najbolji_student} a prosjek mu je {prosjek_najb}")
def studenti_po_smjeru(s,smjer):
    smj=[]
    for student in s:
        if smjer==student['smjer']:
            smj.append(student['ime'])
    return(smj)
def prosjecna_ocjena_po_godinama(r):
    godine={}
    prosjeci={}
    for i in r:
       god=i["godina"]
       pros=i["prosjek"]
       if god not in godine:
           godine[god]=0
           prosjeci[god]=0
       godine[god]+=pros
       prosjeci[god]+=1
    prosjecne_vr={}
    for i in godine:
       prosjecne_vr[i]=(godine[i]/prosjeci[i])
    return prosjecne_vr
'''
'''
#2.Zadatak
n=int(input("unesite n dimenziju matrice:"))
m=int(input("unesite m dimenziju matrice:"))
if n<2 and m<2:
    exit()
else:
    matrica=[]
    for i in range(n):
        red=[]
        for j in range(m):
            red.append(int(input("Unesite element:")))
        matrica.append(red)
    l=len(matrica)
    print(l)
#Prosjecna visina
visina=0
broj_osoba=m*n
for i in range(len(matrica)):
    for j in range (len(matrica[0])):
        visina+=matrica[i][j]
prosjecna_visina_svih=visina/broj_osoba
print(f"Prosjecna visina svih je{prosjecna_visina_svih}")
#Iznad prosjeka
suma=0
for i in range(len(matrica)):
    for j in range (len(matrica[0])):
        if matrica[i][j]>prosjecna_visina_svih:
            suma+=1
print(f"Suma ljudi iznad prosjeka je{suma}")
#Sortiranje po vrstama
matricasortirana=[]
for i in range(len(matrica)):
        for j in range(len(matrica)):
            red=[matrica[i][j].sort(key=lambda x:x[i][j]:reverse=False)]
        red.append(matricasortirana)
        matrica.append(red)
print(matricasortirana)
'''
#3. zadatak 
'''
import csv
f=open("kolokvijum\Studenti.csv")
sadrzaj=csv.DictReader(f)
studenti=[]
for red in sadrzaj:
    if red[4]=='Da':
        studenti.append(red)
f.close()
studenti.sort(key=lambda x: x[3],reverse=True)
f2=open("OdlicniStudenti.csv",'w',newline='')
pisanje=csv.DictWriter(f2,fieldnames=sadrzaj.fieldnames)
pisanje.writeheader()
for student in studenti:
    pisanje.writerow(student)
najbolji_student=student[0]
f2.close()
print(f"Dobitnik stipendije je {najbolji_student}")
print("Zadatak je gotov")
'''
#4.Zadatak 
'''
class Zaposleni:
    def __init__(self, ime, pozicija, plata, aktivan):
        self.ime = ime
        self.pozicija = pozicija
        self.plata = plata
        self.aktivan = True
    def deaktiviraj(self):
        self.aktivan=False
        return (f'Stanje vraceno na false za {self.ime}')
    def povecaj_platu(self,iznos,ime):
        if self.ime==ime:
            self.plata+=iznos
    def __str__(self):
        return (f"Ime:{self.ime},Pozicija:{self.pozicija}, Plata:{self.plata}, aktivan:{self.aktivan}")
class Menadzer(Zaposleni):
    def __init__(self, ime, pozicija, plata, aktivan,broj_timova):
        super().__init__(ime, pozicija, plata, aktivan)
        self.broj_timova=broj_timova
    def povecaj_platu(self, iznos, ime):
        nova=super().povecaj_platu(iznos, ime)+(self.broj_timova*0.5)
        return (nova)
    def __str__(self):
        osnovno = super().__str__()
        return f"{osnovno}, broj  timova:{self.broj_timova}"
class Programer(Zaposleni):
    def __init__(self, ime, pozicija, plata, aktivan,jezici):
        super().__init__(ime, pozicija, plata, aktivan)
        self.jezici=jezici=[]
    def dodaj_jezik(self,jezik):
        if jezik not in self.jezici:
            self.jezici.append(jezik)
            print("Jezik je dodat")
        else:
            print("JEzik nije dodat")
    def __str__(self):
        osnovno = super().__str__()
        return f"{osnovno},jezici{self.jezici}"
zaposleni1=Zaposleni('Marko','sekretar',450,"Da")
menadzer=Menadzer('Mara','glavni men',550,"Da",2)   
programer=Programer('Nikola','programer',850,"Da","Java") 
'''


    

    

