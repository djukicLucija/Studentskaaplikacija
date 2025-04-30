#Zadatak 1
'''
x1=int(input("Unesite x1: "))
y1=int(input("Unesite y1: "))
x2=int(input("Unesite x2: "))
y2=int(input("Unesite y2: "))
x3=int(input("Unesite x3: "))
y3=int(input("Unesite y3: "))

a=((x2-x1)**2+(y2-y1)**2)**0.5
b=((x3-x2)**2+(y3-y2)**2)**0.5
c=((x1-x2)**2+(y1-y2)**2)**0.5

obim=a+b+c
print(f"Obim je {obim}")
'''
#Zadatak 2
'''
x= int(input("Unesite vrijednost x: "))

if x<0:
    y=x**2+2*x+1
elif 0<=x<=5:
    y=x**0.5+3
else:
    y=(2*x**3-x)/(x+1)
print(y)
'''
#Zadatak 3
'''
broj=int(input("Unesite cetvorocifren broj: "))
if broj>9999:
    print("Unijeli ste neodgovarajuci broj.")

prva=broj%10
druga=(broj//10)%10
treca=(broj//100)%10
cetvrta=(broj//1000)
print(f"Rezultat je {(prva+druga+treca+cetvrta)**2}")
'''
#Zadatak 4
'''
n=float(input("Unesite koliko novca imate: "))
x=float(input("Unesite jucerasnju cijenu akcije: "))
novo_x=x*1.15
if novo_x>n:
    print("Ne moze kupiti ni jednu")
broj=0
ostatak=0
while novo_x<=n:
    broj+=1
    ostatak=n-novo_x
    n-=novo_x
print(f"Moze kupiti {broj} dionica, ostaje mu {ostatak}")
'''
#Zadatak 5
'''
a=int(input("Unesite trocifren broj a: "))
b=int(input("Unesite trocifren broj b: "))
if a >999 or b>999:
    print("Unijeli ste broj sa nedovoljno ili previse cifara")
elif a<0 or b<0:
    proizvod=a%10*a//100+b%10*b//100
    print(proizvod)
else:
    zbir=a%10+a//100+b%10+b//100
    print(zbir)
'''
#Zadatak 7
'''
x = int(input("Unesite broj koji zelite da stepenujete:"))
n = int(input("Unesite stepen broja:"))
rezultat = 1
i = 0
while i < n:
    rezultat = rezultat * x
    i = i + 1
print(rezultat)
'''
#Zadatak 8
'''
ulazni_string = input("Unesite neki string:")
rezultat = ""
for karakter in ulazni_string:
    if karakter in "AEIOUaeiou":
        rezultat += karakter
    else:
        continue
print(rezultat)
'''