#1
"""
inventar=[{"ime":"mač","težina":23,"vrijednost":23,"kategorija":"oružije","rijedak":True},
          {"ime":"kramp","težina":44,"vrijednost":44,"kategorija":"alat","rijedak":False},
          {"ime":"odijelo","težina":20,"vrijednost":20,"kategorija":"oklop","rijedak":True},
          {"ime":"mapa","težina":10,"vrijednost":10000,"kategorija":"potrošno","rijedak":True}]
def izračunaj_ukupnu_težinu(r):
    s=0
    for i in r:
        s+=i["težina"]
    return s

def nadji_najvrijedniji_predmet(r):
    s=0
    for i in r:
        if i["vrijednost"]> s:
            s=i["vrijednost"]
            max=i
    return max
def filtriraj_rijetke_predmete(r):
    lista=[]
    for i in r:
        if i["rijedak"]==True:
            lista.append(i)
    return lista
def prosjecna_vrijednost_po_kategorijama(r):
   kategorije={}
   brojevi_kategorija={}
   for i in r:
       kat=i["kategorija"]
       vrij=i["vrijednost"]
       if kat not in kategorije:
           kategorije[kat]=0
           brojevi_kategorija[kat]=0
       kategorije[kat]+=vrij
       brojevi_kategorija[kat]+=1
   prosjeci={}
   for i in kategorije:
       prosjeci[i]=(kategorije[i]/brojevi_kategorija[i])
   return prosjeci
"""
#2
"""
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
    for i in range(l):
        print(matrica[i])
    
    s=0
    max=0
    for i in range(n-1):
        for j in range(m-1):
            s=matrica[i][j]+matrica[i][j+1]+matrica[i+1][j]+matrica[i+1][j+1]
            if max<s:
                max=s
                jed=matrica[i][j]
                dva=matrica[i][j+1]
                tri=matrica[i+1][j]
                cetri=matrica[i+1][j+1]
    print(jed,dva)
    print(tri,cetri)
    print(jed+dva+tri+cetri)"""
#3
"""
import csv
f=open("Knjige.csv")
sadržaj=csv.DictReader(f)
lista=[]
for i in sadržaj:
    if (i["Genre"]=="Fantasy" or i["Genre"]=="Thriller") and float(i["Rating"])>=4.5:
        lista.append(i)
f.close()
lista=lista[:7]
f2=open("TopKnjigice.csv","w",newline="")
pisanje=csv.DictWriter(f2,fieldnames=["Book.ID","Title","Author","Genre","Pages","Rating","Reviews"])
pisanje.writeheader()
for i in lista:
    pisanje.writerow(i)
f2.close()
f3=open("TopKnjigice.csv")
sad=csv.DictReader(f3)
a=float("inf")
for i in sad:
    if int(i["Pages"])<a:
        a=int(i["Pages"])
        min=i
f3.close()
print(min)
"""
#4
"""
class Knjiga:
    def __init__(self,naslov,autor,godina_izdanja,broj_strana):
        self.naslov=naslov
        self.autor=autor
        self.godina_izdanja=godina_izdanja
        self.broj_strana=broj_strana
        self.pozajmljena=False
    def pozajmi(self):
        if self.pozajmljena==True:
            return "Knjigu koju birate da pozajmite nije moguće pozajmiti"
        else:
            self.pozajmljena=True
            return "Knjiga uspješno pozajmljena."
    def vrati(self):
        self.pozajmljena=False
        return "Knjiga uspješno vraćena."
    def status(self):
        return f"Knjiga : {self.naslov},autor:{self.autor},Godina izdanja: {self.godina_izdanja},broj_strana:{self.broj_strana},Status: {"Izdata" if self.pozajmljena==True else "Dostupna"}"
    def __str__(self):
        return f"{self.naslov},{self.autor},{self.godina_izdanja},{self.broj_strana},Status: {"Izdata" if self.pozajmljena==True else "Dostupna"}"
class ElektronskaKnjiga (Knjiga):
    def __init__(self, naslov, autor, godina_izdanja, broj_strana,format,veličina_fajla):
        super().__init__(naslov, autor, godina_izdanja, broj_strana)
        self.format=format
        self.veličina_fajla=veličina_fajla
    def pozajmi(self):
        if self.veličina_fajla<100:
            return super().pozajmi()
        else: 
            return"Greška, nemoguće pozajmiti"
    def kompresuj(self):
        self.veličina_fajla*=0.9
    def __str__(self):
        osnova=super().__str__()
        return f"{osnova},{self.format},{self.veličina_fajla}"
class AudioKnjiga(Knjiga):
    def __init__(self, naslov, autor, godina_izdanja, broj_strana,trajanje,nivo_glasnoće):
        super().__init__(naslov, autor, godina_izdanja, broj_strana)
        self.trajanje=trajanje
        self.nivo_glasnoće=nivo_glasnoće
    def pozajmi(self):
        if 20<=self.nivo_glasnoće<=80:
            return super().pozajmi()
        else:
            return "greška, nije moguće pozajmiti"
    def podesi_glasnoću(self,broj):
        if 0<=broj<=100:
            self.nivo_glasnoće=broj
        else:
            return "Greška, niste validan nivo unjeli"
    def __str__(self):
        Osnova= super().__str__()
        return f"{Osnova},{self.trajanje},{self.nivo_glasnoće}"

k1 = Knjiga("1984", "George Orwell", 1949, 328)
k2 = Knjiga("Na Drini ćuprija", "Ivo Andrić", 1945, 314)
k3 = Knjiga("Ponos i predrasude", "Jane Austen", 1813, 279)

e1 = ElektronskaKnjiga("Digitalni Bastion", "Dan Brown", 1998, 356, "PDF", 95)
e2 = ElektronskaKnjiga("Ubik", "Philip K. Dick", 1969, 240, "EPUB", 110)
e3 = ElektronskaKnjiga("Kafka na obali", "Haruki Murakami", 2002, 505, "MOBI", 89)

a1 = AudioKnjiga("Slušaj me", "David Goggins", 2018, 320, 7.5, 50)
a2 = AudioKnjiga("Sapiens", "Yuval Noah Harari", 2011, 443, 15.2, 85) 
a3 = AudioKnjiga("Mali princ", "Antoine de Saint-Exupéry", 1943, 96, 2.1, 30)

print(k1)
print(e1)
print(a1)

print(a2.pozajmi())
a2.podesi_glasnoću(70)
print(a2.pozajmi())

print(e2.pozajmi())
e2.kompresuj()
print(e2.pozajmi())"
"""