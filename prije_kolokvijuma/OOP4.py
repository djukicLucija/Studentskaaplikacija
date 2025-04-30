import csv
#Zadarak1
'''
f=open("cars.csv")
sadrzaj=csv.DictReader(f)
automobili=[]
godina=input('Unesite zeljenu godinu: ')

for red in sadrzaj:
    automobili.append(red)
f.close()
f2=open("Zadatakgodine.csv","w",newline="")
pisanje=csv.DictWriter(f2,fieldnames=sadrzaj.fieldnames)
pisanje.writeheader()
for auto in automobili:
    if auto["year"]>godina:
        pisanje.writerow(auto)
    else:
        continue
f2.close()
print("Gotovo")
'''
#Zadatak 2
'''
f=open("cars.csv")
sadrzaj=csv.DictReader(f)
prosjecna_cijena_marka={}
broj_kola_marka={}
for auto in sadrzaj:
    model=auto["model"]
    if model in prosjecna_cijena_marka:
        prosjecna_cijena_marka[model]+=int(auto["price"])
        broj_kola_marka[model]+=1
    else:
        prosjecna_cijena_marka[model]=int(auto["price"])
        broj_kola_marka[model]=1
for model in prosjecna_cijena_marka:
    prosjecna_cijena_marka[model]/=broj_kola_marka[model]
    print(f"{model}:{prosjecna_cijena_marka[model]}")
f.close()
'''


#Zadatak 3
'''
f=open("cars.csv")
sadrzaj=csv.DictReader(f)
automobili=[]
for red in sadrzaj:
    automobili.append(red)
f.close()

automobili.sort(key=lambda x:x["horsepower"],reverse=True)


f2=open("Zadatakautomobili3.csv","w",newline="")
pisanje=csv.DictWriter(f2,fieldnames=sadrzaj.fieldnames,)
pisanje.writeheader()
for auto in automobili:
    pisanje.writerow(auto)
f2.close()
print("Zadatak je zavrsen")
'''
#Zadatak 4
'''
f=open("cars.csv")
sadrzaj=csv.DictReader(f)
broj_boja={}
for auto in sadrzaj:
    boja=auto["color"]
    if boja in broj_boja:
        broj_boja[boja]+=1
    else:
        broj_boja[boja]=1
print(broj_boja)
f.close()
boje_i_brojevi=list(broj_boja.items())
boje_i_brojevi.sort(key=lambda x: x[1], reverse=True)
top5_boja=boje_i_brojevi[:5]
f2=open("Top_5_boja.csv","w",newline="")
field_names=["Color","Count"]
pisanje=csv.DictWriter(f2,field_names)
pisanje.writeheader()

for boja,broj in top5_boja:
    pisanje.writerow({"Color":boja,"Count": broj})

f2.close()
'''


