#9. Zadatak-da li se pravougaonici sudaraju
'''
def da_li_se_sudaraju(x1, y1, x2, y2, x3, y3, x4, y4):
    # Ako je jedan pravougaonik potpuno lijevo od drugog
    if x2 < x3 or x4 < x1:
        return False
    # Ako je jedan pravougaonik potpuno iznad drugog
    if y1 > y4 or y3 > y2:
        return False
    # Inače se pravougaonici sudaraju
    return True
print("Unesite koordinate za prvi pravougaonik (gornja lijeva i donja desna tačka):")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
print("Unesite koordinate za drugi pravougaonik (gornja lijeva i donja desna tačka):")
x3 = float(input("x3: "))
y3 = float(input("y3: "))
x4 = float(input("x4: "))
y4 = float(input("y4: "))
if da_li_se_sudaraju(x1, y1, x2, y2, x3, y3, x4, y4):
    print("Pravougaonici se sudaraju.")
else:
    print("Pravougaonici se ne sudaraju.")
'''
#10 Zadatak
'''
def broj_novcica_unutar_radijusa(novcici, igrac_pozicija, radijus):
    px, py = igrac_pozicija
    count = 0
    for x, y in novcici:
        # Računanje udaljenosti između igrača i novčića
        udaljenost = ((x - px) ** 2 + (y - py) ** 2) ** 0.5
        if udaljenost <= radijus:
            count += 1
    return count
# Primjer podataka
novcici = [(1, 2), (3, 4), (5, 6), (2, 2), (4, 3)]
igrac_pozicija = (3, 3)
radijus = 2
# Računanje i ispis rezultata
rezultat = broj_novcica_unutar_radijusa(novcici, igrac_pozicija, radijus)
print(f"Broj novčića koje igrač može da pokupi: {rezultat}")
'''
#Zadatak 11
'''
def pr_sa_najvecom_p(pravougaonici):
    najveca_p=0
    a=0
    b=0
    for pravougaonik in pravougaonici:
        povrsina=pravougaonik[0]*pravougaonik[1]
        if najveca_p<povrsina:
            najveca_p=povrsina
            a=pravougaonik[0]
            b=pravougaonik[1]
    return f"Najveca povrsina je {najveca_p},a stranice su mu: {a} i {b}"
pravougaonici = [(3, 4), (5, 2), (6, 7), (4, 4), (2, 10)]
print(pr_sa_najvecom_p(pravougaonici))
'''
#Zadatak 14 -najvrijedniji predmet
'''
predmeti=[{"ime":"lopta","tezina":1,"vrijednost":5},
          {"ime":"medo","tezina":2,"vrijednost":10},
          {"ime":"laser","tezina":0.5,"vrijednost":1.5}]
def ukupna_tezina(predmeti):
    tezina=0
    for predmet in predmeti:
        tezina+=predmet["tezina"]
    return f"Ukupna tezina je {tezina}"
def najvrijedniji(predmeti):
    najvrijedniji_vr=0
    najvr_predmet=""
    for predmet in predmeti:
        if najvrijedniji_vr<predmet["vrijednost"]:
            najvrijedniji_vr=predmet["vrijednost"]
            najvr_predmet=predmet["ime"]
    return f"Najvrijedniji predmet je {najvr_predmet} a vrijednost mu je {najvrijedniji_vr}"

print(ukupna_tezina(predmeti))
print(najvrijedniji(predmeti))
'''
#Zadatak 15
'''
import math
NPC_likovi=[{"ime": "MM1", "uloga":"snajperista", "pozicija":(2,3), "zadaci":['setnja','straza']},
          {"ime": "MI1", "uloga":"vojnik", "pozicija":(3,4), "zadaci":['pucanje','trk']},
          {"ime": "MN1", "uloga":"pjesadinac", "pozicija":(1,5), "zadaci":['strazarenje','pucanje']}]
def dodaj_zadatak(lista,ime, zadatak):
    for npc in lista:
        if npc["ime"]==ime:
            npc["zadaci"].append(zadatak)
            print(f'Zadatak {zadatak} je dodat')        
def najblizi_poziciji(lista,pozicija):
    min_udaljenost = float('inf')
    najblizi = None
    for npc in lista:
        npc_poz = npc["pozicija"]
        udaljenost = math.dist(pozicija, npc_poz)
        if udaljenost < min_udaljenost:
            min_udaljenost = udaljenost
            najblizi = npc
    return najblizi
print(dodaj_zadatak(NPC_likovi, "MN1", "Patroliraj po zidu"))
print(najblizi_poziciji(NPC_likovi,(1,4)))
'''
#16. zadatak - status zadatka zavrseno
'''
zadaci=[{"naziv":"pranje sudova", "status": "nezavrseno","nagrada":1},
        {"naziv":"pranje vesa", "status": "nezavrseno","nagrada":2},
        {"naziv":"usisavanje", "status": "zavrseno","nagrada":3}]
def mijenjanje_statusa(lista,naziv):
    for zadatak in zadaci:
        if naziv==zadatak["naziv"]:
            zadatak["status"]="zavrseno"
            print(f"Za zadatak {zadatak}, apdejtovan status")
            return True
        return False
def ukupna_nagrada_za_zavrsene(lista):
    u_n=0
    for zadatak in lista:
        if zadatak["status"]=="zavrseno":
            u_n+=zadatak["nagrada"]
    return f'Ukupna nagrada je {u_n}'
print(mijenjanje_statusa(zadaci,"pranje sudova"))
print(ukupna_nagrada_za_zavrsene(zadaci))
'''
#18. zadatak pretvaranje stringa u listu brojeva
'''
ulaz = "30;150;250;40;90"
# Pretvori string u listu brojeva (int)
zanrovi = [int(broj) for broj in ulaz.split(";")]
# Filtriraj samo žanrove koji imaju 100 ili više filmova
filtrirani = [broj for broj in zanrovi if broj >= 100]
# Računaj prosjek i prikaži kao cijeli broj
if filtrirani:
    prosjek = sum(filtrirani) // len(filtrirani)
    print(prosjek)
else:
    print(0)
'''
#19. Zadatak prisustvo
'''
studenti= [{"ime":"Marko Markovic","prisutan":10,"odustan":2},
           {"ime":"Milos Milosevic","prisutan":8,"odustan":4}, 
           {"ime":"Marija Cetkovic","prisutan":6,"odustan":6},
           {"ime":"Nikola Milivojevic","prisutan":2,"odustan":10},
           {"ime":"Marijana Minic","prisutan":11,"odustan":1}]   
def pravo_izlaska(lista):
    mogu_izaci=[]
    for student in lista:
        pr=student["prisutan"]/(student["prisutan"]+student['odustan'])
        if pr>0.74:
            mogu_izaci.append((student["ime"],round(pr,2)))
    return(mogu_izaci)

print(pravo_izlaska(studenti))
'''

