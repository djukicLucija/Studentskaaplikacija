#prikaz izuzetaka
'''
try:
    rezultat=10/0
except ZeroDivisionError:
    print("Greska. Nije dozvoljeno dijeljenje sa nulom.")
print(10)
'''
'''
try:
    broj=int(input("Unesite vrijednost: "))
    print(broj)
except ValueError:
    print("Niste unijeli ispravnu vrijednost")
'''
'''
try:
    broj=int(input("Unesite vrijednost: "))
    print(broj)
except Exception as e:
    print(e)
print(10)
'''
'''
def provjeri_godine(godine):
    if godine<18:
        raise ValueError("Morate imati najmanje 18 godina.")
    return "Pristup odobren"
try:
    unos_godina=int(input("Unesite godine:"))
    rezultat=provjeri_godine(unos_godina)
    print(rezultat)
except Exception as e:
    print (e)
'''
'''
try:
    list=[1,2,3]
    indeks=int(input("Unesite indeks:"))
    print(list[indeks])
except IndexError:
    print("Unijeli ste indeks izvan opsega.")
except ValueError:
    print("Niste unijeli cijeli broj.")'
'''
#list comprehension
'''
list_squares=[x**2 for x in range(1,101)]
print(list_squares)'
'''
'''
list=[x**2%5 for x in range(1,101)]
print(list)'
'''
'''
lista_filmova=["The Goodfather","Pulp Fiction","The wizard of Oz"]
lista_nat=[film for film in lista_filmova if  film.lower().startswith("t")]
print(lista_nat)
'''
'''
movi=[("The Goodfather",1972),("Pulp Fiction",1994),("The wizard of Oz",1990)]
lista_nakon1990=[film[0]for film in movi if film[1]>1990]
print(lista_nakon1990)'
'''
'''
lista=[10,20,30]
nova_lista=[element*3 for element in lista]
print(nova_lista)'
'''
#rekurzija
'''
def suma_n(n):
    if n==1:
        return 1
    return n+suma_n(n-1)
print(suma_n(5))
'''
'''
func= lambda a,b: a+b
print(func(2,3))'
'''