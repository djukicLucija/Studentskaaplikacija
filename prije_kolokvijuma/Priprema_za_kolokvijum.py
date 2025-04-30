#1. Zadatak
'''
inventar = [
    {"ime": "Kasika", "tezina": "4", "vrijednost": 5, "kategorija": "posudje", "rijedak": False},
    {"ime": "Mac", "tezina": "10", "vrijednost": 50, "kategorija": "oruzje", "rijedak": False},
    {"ime": "Dijamant", "tezina": "1", "vrijednost": 5000, "kategorija": "nakit", "rijedak": True}
]

def izracunaj_ukupnu_tezinu_inventara(inventar):
    rezultat = 0
    for predmet in inventar:
        rezultat += int(predmet["tezina"])
    return rezultat

def nadji_najvrijedniji_predmet(inventar):
    najvrijedniji = inventar[0]
    for predmet in inventar:
        if predmet["vrijednost"] > najvrijedniji["vrijednost"]:
            najvrijedniji = predmet
    return najvrijedniji

def filtriraj_rijetke_predmete(inventar):
    rijetki_predmeti = []
    for predmet in inventar:
        if predmet["rijedak"]:
            rijetki_predmeti.append(predmet)
    return rijetki_predmeti
def prosjecna_vrijednost_po_kategorijama(inventar):
    zbir_vrijednosti = {}
    broj_predmeta = {}

    for predmet in inventar:
        kategorija = predmet["kategorija"]
        vrijednost = predmet["vrijednost"]

        if kategorija in zbir_vrijednosti:
            zbir_vrijednosti[kategorija] += vrijednost
            broj_predmeta[kategorija] += 1
        else:
            zbir_vrijednosti[kategorija] = vrijednost
            broj_predmeta[kategorija] = 1

    prosjeci = {}
    for kategorija in zbir_vrijednosti:
        prosjeci[kategorija] = zbir_vrijednosti[kategorija] / broj_predmeta[kategorija]

    return prosjeci
print(izracunaj_ukupnu_tezinu_inventara(inventar))
print(nadji_najvrijedniji_predmet(inventar))
'''
#2. zadatak
'''
def unesi_matricu(n, m):
    matrica = []
    print("Unesite elemente matrice red po red:")
    for i in range(n):
        red = []
        for j in range(m):
            vrijednost = int(input(f"Element [{i}][{j}]: "))
            red.append(vrijednost)
        matrica.append(red)
    return matrica

def nadji_najveci_2x2_blok(matrica, n, m):
    max_suma = float('-inf')
    max_blok = []

    for i in range(n - 1):
        for j in range(m - 1):
            blok = [
                [matrica[i][j], matrica[i][j + 1]],
                [matrica[i + 1][j], matrica[i + 1][j + 1]]
            ]
            suma = sum(sum(red) for red in blok)

            if suma > max_suma:
                max_suma = suma
                max_blok = blok

    return max_blok, max_suma
n = int(input("Unesite broj redova (n >= 2): "))
m = int(input("Unesite broj kolona (m >= 2): "))

if n < 2 or m < 2:
    print("Matrica mora imati najmanje dimenzije 2x2.")
else:
    matrica = unesi_matricu(n, m)
    najbolji_blok, suma = nadji_najveci_2x2_blok(matrica, n, m)

    print("\nNajveća 2x2 podmatrica je:")
    for red in najbolji_blok:
        print(red)
    print("Ukupna suma:", suma)
'''
#3. zadatak
import csv
f = open("knjige.csv", ) 
sadrzaj = csv.DictReader(f)
knjige = []
for red in sadrzaj:
    knjige.append(red)
f.close()  
knjige.sort(key=lambda x: float(x["Rating"]), reverse=True)



