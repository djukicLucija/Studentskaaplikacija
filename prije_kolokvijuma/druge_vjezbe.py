#1. zadatak
'''def pretrazi(lista):
  bodovi=0
  karakter=0
  for karakter in lista:
      if karakter == "1":
        bodovi+=1
      elif karakter == "*":
        bodovi-=1
      elif karakter == "0":
        continue
      else:
        print("Nepoznati karakter")
        
    return(bodovi)'''
'''
#2. zadatak
#1
x1=3
y1=5
x2=2
y2=4
#2
x3=3
y3=10
x4=7
y4=6

def podudaranje(x1,y1,x2,y2,x3,y3,x4,y4:
                if x1>x4

'''
#3. zadatak
'''
pravugaonici=[(10,4),(14,5),(15,15)]

def povrsina( pravougaonici):
    najveci=pravougaonici[0]
    najveca_povrsina=najveci[0]*najveci[1]

    for pravugaonik in pravugaonici[1:]:
        povrsina=pravugaonik[0]*pravugaonik[1]
        if povrsina>najveca_povrsina:
            najveca_povrsina=povrsina
            najveci=pravugaonik
    return najveci
print(povrsina(pravugaonici))
test=povrsina(pravugaonici)
print(test[0]*test[1])
'''
'''
#4. zadatak

def broj_novcica(px,py,r novcici):
    broj=0
    for x,y in novcici:
        euklidsko=((px-x)**2+(py-y)**2)**0.5
        if euklidsko <=r:
            broj+=1
        return broj
novcici= [(1,2),(3,4),(5,6),(7,8)]
px, py=3,3
r=2
rezultat= broj_novcica(px,py,r,novcici)
print(f"Igrac moze da pokupi {rezultat} novcica")
'''