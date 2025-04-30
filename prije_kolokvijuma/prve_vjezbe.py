
#Zadatak 1

x1= int(input("Unesite x1 vrijednost prve tacke: "))
y1= int(input("Unesite y1 vrijednost prve tacke: "))
x2= int(input("Unesite x2 vrijednost druge tacke: "))
y2= int(input("Unesite y2 vrijednost druge tacke: "))
x3= int(input("Unesite x3 vrijednost trece tacke: "))
y3= int(input("Unesite y3 vrijednost trece tacke: "))

a=((x2-x1)**2+(y2-y1)**2)**0.5
b=((x3-x1)**2+(y3-y1)**2)**0.5
c=((x3-x2)**2+(y3-y2)**2)**0.5

O= a+b+c
print(f"Obim stola je {O}")

#Zadatak 2

x= int(input("Unesite vrijednost x: "))
if x < 0:
    print(x**2+x+1)
elif  0<= x <= 5:
    print(x**0.5+3)
else :
    print((2*x**3-x)/(x+1))
''''
#Zadatak 3

x= int(input("Unesite cetborocifreni  broj n: "))
c1=n//1000
c1=(n//100)%10
c3=(n//10)%10
c4=n%10

rezultat=(c1+c2+c3+c4)**2
print(f"Rezultat je {rezultat}")

#Zadatak 4

n= float(input("Unesite budzet n: "))
x= float(input("Unesite cijenu: "))
broj=0
nova_cijena=x*1.15

if n>=nova_cijena:
    print(f"Broker moze da kupi:{n//nova_cijena} akcija.")
else:
    print("Ne moze da kupi akcije")

#Zadatak 7

x=int(input("Unesite broj x: "))
n=int(input("Unesite stepen: "))

rezultat=1
i=0
while(i<n):
    rezultat=rezultat*x
    i=i+1
print(rezultat)

#Zadatak 8

ulazni_string=input("Unesite neki string: ")
rezultat=""
for karakter in ulazni_string:
    if karakter in "AEIOU":
        rezultat+=karakter
    


 
'''