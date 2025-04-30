#Prvi zadatak
'''
lista_filmova = [{"naziv":"The Godfather", "br_pozitivni":1000,"br_negativni":10}, 
                {"naziv":"The Pianist", "br_pozitivni":500,"br_negativni": 30},
                {"naziv":"A Beautiful Mind", "br_pozitivni":600,"br_negativni": 45}]

najbolji_film=lista_filmova[0]
for film in lista_filmova:
    if najbolji_film["br_pozitivni"]<film["br_pozitivni"]:
        najbolji_film= film
print(najbolji_film)
termin=input("Unesite term:")
for film in lista_filmova:
  #  if film["naziv"][0:len(termin)]==termin:
    if film["naziv"].lower().startswith(termin.lower()):
        print(film)
najbolji_odnos_filmovi=lista_filmova[0]["br_pozitivni"]/lista_filmova[0]["br_negativni"]
najbolji_film=lista_filmova[0]
for film in lista_filmova:
    odnos=film["br_pozitivni"]/film["br_negativni"]
    if odnos> najbolji_odnos_filmovi:
        najbolji_odnos_filmovi=odnos
        najbolji_film=film
print(najbolji_film)
'''
#1 zadatak
#Zbir elemenata sa glavne dijagonale
'''
matrica=[[10,12,5],[3,7,9],[12,3,-5]]
suma=0
for i in range(len(matrica)):
    for j in range(len(matrica[0])):
        if i==j:
            suma+=matrica[i][j]
print(suma)
'''
#2 zadatak
'''
slika_5_5=[[0,0,0,0,0],
           [0,255,255,255,0],
           [0,255,255,255,0],
           [0,255,255,255,0],
           [0,0,0,0,0]]
for i in range(len(slika_5_5)):
    for j in range (len(slika_5_5)):
        if slika_5_5[i][j]==0:
            slika_5_5[i][j]=255
        else:
           slika_5_5[i][j]=0
print(slika_5_5)
'''
#3 zadatak
A=[[1,2,3],[4,5,6],[7,8,9]]
B=[[-1,-2,-3],[-4,-5,-6],[-7,-8,-9]]
C=[]
for i in range(len(A)):
    red=[]
    for j in range (len(A[0])):
        red.append(0)
    C.append(red)
for i in range(len(A)):
    for j in range (len(A[0])):
        C[i][j]=A[i][j]+B[i][j]
print(C)


    





 