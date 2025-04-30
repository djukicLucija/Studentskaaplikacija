#1.zadatak -grad sa najmanjim brojem stanovnika
'''
def grad(fajl,drzava):
    najmanje=100000000000000
    najm_grad=""
    f=open(fajl)
    linija=f.read().split("\n")
    f.close()
    for red in linija:
        razdvojeno=red.split(",")
        if razdvojeno[0]==drzava:
            populacija= int(razdvojeno[2])
            if populacija<najmanje:
                najmanje=populacija
                najm_grad=razdvojeno[1]
    return f"Grad sa najmanjim brojem stanovnika za drzavu {drzava} je {najm_grad}"
'''
#2.zadatak 
'''
def broj_stanovnika(fajl,drzava):
    f=open(fajl)
    linija=f.read().split("\n")
    f.close()
    drzava1=0
    for red in linija:
        razdvojeno=red.split(",")
        if razdvojeno[0]==drzava:
            drzava1=int(razdvojeno[2])
    return drzava1
'''
#3.zadatak
'''
def prosjek(fajl,grad):
    suma=0
    broj=0
    f=open(fajl)
    redovi=f.read().split("\n")
    f.close()

    for red in redovi:
        podaci= red.split(",")
        if podaci[0]==grad:
            suma+=int(podaci[2])
            broj+=1

    prosjek=suma/broj
    return f"Prosjecan broj godina za grad {grad} je {prosjek}"
fajl="4.txt"
grad=input("Unesi grad")
print(prosjek(fajl,grad))
'''
#4. zadatak koliko puta se rijec pojavljuje
'''
def broj_rijeci(fajl):
    rjecnik={}
    f=open(fajl)
    rijeci=f.read().lower().split()
    f.close()
    for rijec in rijeci:
        if rijec in rjecnik:
            rjecnik[rijec]+=1
        else:
            rjecnik[rijec]=1
    return rjecnik
fajl="5.txt"
print(broj_rijeci(fajl))
'''
#5. zadatak izuzeci
'''
try:
    rezultat = 10 / 0
    print(rezultat)
except ZeroDivisionError:
    print("Greska. Nije dozvoljeno dijeljnje sa 0")
print(10)
'''
'''
try:
    broj = int(input("Unesite vrijednost:"))
    print(broj)
except Exception as e:
    print(e)
print(10)'
'''
'''
def provjeri_godine(godine):
    if godine < 18:
        raise ValueError("Morate imate najmanje 18 godina.")
    return "Pristup odobren"
try:
    unos_godina = int(input("Unesite godine:"))
    rezulat = provjeri_godine(unos_godina)
    print(rezulat)
except Exception as e:
    print(e)'
'''
'''
try:
    lista = [1,2,3]
    indeks = int(input("Unesite indeks:"))
    print(lista[indeks])
except IndexError:
    print("Unijeli ste indeks van opsega")
except ValueError:
    print("Niste unijeli cijeli broj")'
'''
#6. skracene funkcije i lambda
'''
list_squares = [i**2 for i in range(1,101)]
print(list_squares)
'''
'''
lista = []
for i in range(1, 101):
    lista.append(i ** 2)
'''
'''
list_squares_mod5 = [i**2 % 5 for i in range(1,101)]
print(list_squares_mod5)'
'''
'''
lista_filmova = ["The Godfather", "Pulp Fiction", "The wizard of Oz"]
nova_lista_filmova = []
for film in lista_filmova:
    if film.lower().startswith("t"):
        nova_lista_filmova.append(film)

lista_filmova_slovo_t = [film for film in lista_filmova if film.lower().startswith("t")]
print(lista_filmova_slovo_t)
'''
'''
filmovi = [("The Godfather",1972), ("Pulp Fiction",1994), ("The wizard of Oz",1939)]
filtirana_lista = [film[0] for film in filmovi if film[1] > 1990]
print(filtirana_lista)
'''
'''
lista = [10, 20, 30]
nova_lista = [element * 3 for element in lista]
print(nova_lista)'
'''
''''
def suma_n(n):
    if n == 1:
        return 1
    return n + suma_n(n-1)

print(suma_n(5))

func = lambda a,b: a+b
print(func(2,3))'
'''
'''
def kvadriraj(x):
    return x ** 2

lambda_kvadriraj = lambda x: x ** 2

print(kvadriraj(5))
print(lambda_kvadriraj(5))

# f = a * x * x + b * x + c
def kreiraj_kvadratnu_funkciju(a, b, c): # higher-order funkcija
    d = 10
    return lambda x: a * x * x + b * x + c +d
f = kreiraj_kvadratnu_funkciju(2, 3, -5)
print(f(0))
print(f(5))
print(f(-3))
'''

'''
def func(x):
    return x % 5 == 0
lista = [10, 15, 20, 24, 37]
lista_nova = filter(func, lista)
print(list(lista_nova))'
'''
'''
lista_studenata = [{"ime":"Ana", "prezime":"Markovic"},
                   {"ime":"Nikola", "prezime":"Nikolic"},
                   {"ime":"Jovan", "prezime":"Jovanovic"}]

nova_lista_studenata = filter(lambda x:x["ime"].startswith("A"),lista_studenata)
print(list(nova_lista_studenata))
'''
'''
lista_gradova = [("Podgorica", 17),
                 ("Niksic", 12),
                 ("Andrijevica", 6)]

nova_lista_gradova = map(lambda x:(x[0], 9/5 * x[1] + 32), lista_gradova)
print(list(nova_lista_gradova))'
'''
'''
l1 = [10, 20, 30]
l2 = [5, 10, 15]
l3 = map(lambda x,y:x + y, l1, l2)
print(list(l3))
'''



