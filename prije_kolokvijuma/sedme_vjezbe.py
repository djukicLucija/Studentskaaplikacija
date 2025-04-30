#1 zadatak
'''
def kvadriraj(x):
    return x**2
lambda_kvadriraj=lambda x: x**2
print(kvadriraj(5))
print(lambda_kvadriraj(5))
'''

#2 zadatak
#f=a*x*x+b*x+c
'''
def kreiraj_kvadratnu_funkciju(a,b,c):
    return lambda x:a*x*x+b*x+c
f=kreiraj_kvadratnu_funkciju(2,3,-5)
print(f(0))'
'''
#3 zadatak
'''
def func(x):
    return x%5==0
l=[10,15,20,24,37]
l1=filter(func,l)
#l1=filter(lambda x:x%5==0,l)
print(list(l1))'
'''
#4 zadatak
#lista dict cije ime pocinje na a
'''
l=[{"ime":"Marko","prezime":"Milic"},{"ime":"Arkan","prezime":"Milic"},{"ime":"Anto","prezime":"Maric"}]
l1=filter(lambda x:x["ime"].startswith("A"),l)
print(list(l1))
'''
#5 zadatak
#lista gradova sa t, pretvoriti  celzijuse u feranhajte
#f:9/5*c+32
'''
l=[("Niksic",16),
   ("Podgorica",20),
   ("Andrijevica",6)]
l1=map(lambda x:(x[0],9/5*x[1]+32),l)
print(list(l1))
'''
#6. zadatak
#sabrati elemente dvije liste
'''
l=[1,2,3,4]
l1=[1,2,3,4]
l2=map(lambda x,x1:x+x1,l,l1)
print(list(l2))
'''
#7. zadatak

from functools import reduce
'''
a=[1,2,3,4]
suma=reduce(lambda x, y:x+y,a)
print(suma)
'''
'''
a=[1,2,3,4]
max=reduce(lambda x,y: x if x>y else y,a)
print(max)'
'''
