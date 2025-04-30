import csv
#Zadatak1
'''
f=open("pjesme.csv")
sadrzaj=csv.DictReader(f)
pjesme=[]
for red in sadrzaj:
    pjesme.append(red)
f.close()

pjesme.sort(key=lambda x:x["Length"],reverse=True)
top10=pjesme[:10]

f2=open("Zadatak1.csv","w",newline="")
pisanje=csv.DictWriter(f2,fieldnames=sadrzaj.fieldnames,)
pisanje.writeheader()
for pjesma in top10:
    pisanje.writerow(pjesma)
f2.close()
print("Zadatak je zavrsen")
'''
#Zadatak2
'''
f=open("pjesme.csv")
sadrzaj=csv.DictReader(f)
pjesme=[]
for red in sadrzaj:
    pjesme.append(red)
f.close()
pjesme.sort(key=lambda x:x['Danceability'], reverse=True)
top10=pjesme[:10]
f2=open("Zadatak2.csv","w",newline="")
pisanje=csv.DictWriter(f2,fieldnames=sadrzaj.fieldnames)
pisanje.writeheader()
for pjesma in top10:
    pisanje.writerow(pjesma)
f2.close()
print("Zadatak je zavrsen")
'''
#Zadatak2.1
'''
f=open("pjesme.csv")
sadrzaj=csv.DictReader(f)
pjesme=[]
for red in sadrzaj:
    info_pjesme={
        "Ime pjesme": red['Track.Name'],
        "Ime izvodjaca":red['Artist.Name'],
        "Ritam":red['Danceability']
    }
    pjesme.append(info_pjesme)
f.close()
pjesme.sort(key=lambda x:x["Ritam"],reverse=True)
top10ritmicki=pjesme[:10]   
f2=open("Zadatak2.1.csv","w",newline="")
pisanje=csv.DictWriter(f2,fieldnames=["Ime pjesme","Ime izvodjaca","Ritam"])
pisanje.writeheader()
for red in top10ritmicki:
    pisanje.writerow(red)
f2.close()
print("Zadatak gotov")
'''
#Zadatak3
'''
f=open("pjesme.csv")
sadrzaj=csv.DictReader(f)
pjesme=[]
for red in sadrzaj:
    if red["Track.Name"].isupper:
        info_pjesme={
            "Ime pjesme":red["Track.Name"],
            "Ime izvodjaca": red["Artist.Name"],
            "Popularnost":red["Popularity"],
            "Energicnost":red["Energy"]
            }
        pjesme.append(info_pjesme)
f.close()
pjesme.sort(key=lambda x: x["Popularnost"],reverse=True)
top10popularnost=pjesme[:10]
top10popularnost.sort(key=lambda x: x["Energicnost"],reverse=True)

f2=open("Zadatak3.csv","w",newline="")
pisanje=csv.DictWriter(f2,fieldnames=["Ime pjesme","Ime izvodjaca","Popularnost","Energicnost"])
pisanje.writeheader()
for red in top10popularnost:
    pisanje.writerow(red)
f2.close()
print("Zadatak 3 je gotov")'
'''
#Zadatak4
'''
f=open("pjesme.csv")
sadrzaj=csv.DictReader(f)
pjesme={}
for red in sadrzaj:
    zanr=red["Genre"]
    if zanr in pjesme:
        pjesme[zanr]+=1
    else:
        pjesme[zanr]=1
f.close()

print(pjesme)
'''
