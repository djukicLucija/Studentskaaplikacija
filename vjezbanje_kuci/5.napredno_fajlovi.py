#1. zadatak 10 najduzih pjesama
'''
f=open("pjesme.csv")
sadrzaj=csv.DictReader(f)
pjesme=[]
for red in sadrzaj:
    pjesme.append(red)
f.close()
pjesme.sort(key=lambda x: x['Length'],reverse=True)
top10najduzih=pjesme[:10]
f2=open("Zadatak1.csv",'w',newline='')
pisanje=csv.DictWriter(f2,fieldnames=sadrzaj.fieldnames)
pisanje.writeheader()
for pjesma in top10najduzih:
    pisanje.writerow(pjesma)
f2.close()
print("Zadatak 1 uspjesno zavrsen")
'''
#2. zadatak 
'''
f=open("pjesme.csv")
sadrzaj=csv.DictReader(f)
pjesme=[]

for red in sadrzaj:
    info_pjesme={
        "Ime pjesme":red["Track.Name"],
        "Ime izvodjaca":red["Artist.Name"],
        "Ritam":red["Danceability"]
    }
    pjesme.append(info_pjesme)

f.close()
pjesme.sort(key=lambda x: x['Ritam'],reverse=True)
top10ritmicki=pjesme[:10]

f2=open("Zadatak2.csv","w",newline='')
pisanje=csv.DictWriter(f2,fieldnames=["Ime pjesme","Ime izvodjaca","Ritam"])
pisanje.writeheader()

for red in top10ritmicki:
    pisanje.writerow(red)

f2.close
print("Zadatak2 odradjen")
'''
#3. Zadatak najpopularnijih po energicnosti
'''
import csv
f=open("pjesme.csv")
sadrzaj=csv.DictReader(f)
pjesme=[]

for red in sadrzaj:
    if red["Track.Name"][0].isupper():
        pjesme_info={
            "Ime":red["Track.Name"],
            "Izvodjac":red["Artist.Name"],
            "Popularnost":red["Popularity"],
            "Energicnost":red["Energy"]}
        
        pjesme.append(pjesme_info)

f.close()

pjesme.sort(key=lambda x: x['Popularnost'],reverse=True)
top10popularnih=pjesme[:10]

top10popularnih.sort(key=lambda x: x['Energicnost'],reverse=True)

f2=open("Zadatak3.csv","w",newline="")
pisanje=csv.DictWriter(f2,fieldnames=["Ime","Izvodjac","Popularnost","Energicnost"])
pisanje.writeheader()
for pjesma in top10popularnih:
    pisanje.writerow(pjesma)

f2.close

print("Zadatak 3 je rijesen")
'''
#4.zadatak koliko pjesama pripada kom zanru
"""import csv
import matplotlib.pyplot as plt

f=open("pjesme.csv")
sadrzaj=csv.DictReader(f)
broj_pjesama_po_zanru={}

for red in sadrzaj:
    zanr=red["Genre"]
    if zanr in broj_pjesama_po_zanru:
        broj_pjesama_po_zanru[zanr]+=1
    else:
        broj_pjesama_po_zanru[zanr]=1
f.close()
print(broj_pjesama_po_zanru)"""
#5.zadatak proizvedeni nakon unesene godine
'''import csv

f=open("cars.csv")
podaci=csv.DictReader(f)
filtrirani=[]
godina=int(input("Unesi godinu za filter auta"))
for auto in podaci:
    if int(auto["year"])>=godina:
        filtrirani.append(auto)
f.close()
f2=open("FiltriranaAuta.csv","w",newline="")
pisanje=csv.DictWriter(f2,fieldnames=podaci.fieldnames)
pisanje.writeheader()
for autic in filtrirani:
    pisanje.writerow(autic)
f2.close()
print("Zadatak zavrseno")'''
#6.zadatak prosjecna cijena automobila za svaku marku
"""import csv
f = open("cars.csv")
podaci = csv.DictReader(f)
cijene_po_markama = {}
broj_auta_po_markama = {}
for auto in podaci:
    marka = auto["brand"]
    cijena = int(auto["price"]) 
    if marka in cijene_po_markama:
        cijene_po_markama[marka] += cijena
        broj_auta_po_markama[marka] += 1
    else:
        cijene_po_markama[marka] = cijena
        broj_auta_po_markama[marka] = 1
f.close()
prosjecne_cijene = {}
for marka in cijene_po_markama:
    prosjecna_cijena = cijene_po_markama[marka] / broj_auta_po_markama[marka]
    prosjecne_cijene[marka] = prosjecna_cijena
for marka, prosjecna_cijena in prosjecne_cijene.items():
    print(f"{marka}: {prosjecna_cijena:.2f}")
print("Zadatak završen")"""
#7. zadatak 5 najcescih boja automobila
"""import csv
f = open("cars.csv")
podaci = csv.DictReader(f)
broj_boja = {}
for auto in podaci:
    boja = auto['color']
    if boja in broj_boja:
        broj_boja[boja] += 1
    else:
        broj_boja[boja] = 1
f.close()
boje_i_brojevi = list(broj_boja.items())
boje_i_brojevi.sort(key=lambda x: x[1], reverse=True)
top5_boja = boje_i_brojevi[:5]
f2 = open("top5_colors.csv", "w", newline="")
fieldnames = ['color', 'count']
pisanje = csv.DictWriter(f2, fieldnames=fieldnames)
pisanje.writeheader()
for boja, broj in top5_boja:
    pisanje.writerow({'color': boja, 'count': broj})
f2.close()
print("Zadatak završen")"""
#8.zadatak 
"""import csv
f=open("cars.csv")
podaci=csv.DictReader(f)
konjske=[]
for auto in podaci:
    konjske.append(auto)
konjske.sort(key=lambda x:x['horsepower'],reverse=True)
f.close()
f2=open("Zadatak4.csv","w",newline="")
pisanje=csv.DictWriter(f2,fieldnames=podaci.fieldnames)
pisanje.writeheader()
for auto in konjske:
    pisanje.writerow(auto)
f2.close()
print("Gotovo")"""