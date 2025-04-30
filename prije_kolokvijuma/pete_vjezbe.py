#1 zadatak
'''
A=[[1,2],[1,2]]

def is_square(a):

   if len(a)==len(a[0]) and len(a)>0:
    print("Matrica je kvadratna")
   else:
    print("Matrica nije kvadranta")

is_square(A)
'''
#2 zadatak
'''
def matrica(broj_redova, broj_kolona):
    m=[]
    for i in range(broj_redova):
          s=[]
          for j in range (broj_kolona):
              s.append(int(input("Unesite element: ")) ) 
          m.append(s)
    print(m)

matrica(3,3)
'''
#3. zadatak
'''
studenti=[{"ime":"Marko Mirkovi", "prisutan":8,"odsutan":7},
          {"ime":"Marko Mirkoc", "prisutan":4,"odsutan":11},
          {"ime":"Marko Movic", "prisutan":11,"odsutan":4},
          {"ime":"Marko Miovic", "prisutan":15,"odsutan":0},]

for student in studenti:
    procenat=student["prisutan"]/15
    if procenat>=0.75:
       student["prisutan"]="Ima pravo izlaska"
       student["odsutan"]=round(procenat*100,2)
    else:
        student["prisutan"]="Nema pravo izlaska"
        student["odsutan"]=round(procenat*100,2)
print(studenti)
'''
#4.zadatak
'''
m=[[1,5,4],[3,2,2],[7,5,1]]
def matrix_even(m):
  broj=0
  for i in range(len(m)):
    for j in range(1,len(m),2):
       if m[i][j]%2!=0:
         broj+=1
  print(broj)
m=[[1,5,4],[3,2,2],[7,5,1]]
matrix_even(m)
'''
#5.zadatak

a=[[1,2,3],[2,2,3]]


             


