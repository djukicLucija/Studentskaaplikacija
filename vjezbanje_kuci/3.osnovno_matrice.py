#1 zadatak -zbir po dijagonali
'''
m = [[10,12,5],[3,7,9],[12,3,-5]]
br_vrsta=len(m)
br_kolone=len(m[0])
suma=0
for i in range(len(m)):
    for j in range (len(m[0])):
        if i==j:
            suma+=m[i][j]
print(suma)
'''           
#2. zadatak- je li matrica kvadratna
''' 
m = [[10,12,5],[12,3,-5]]
def is_square(m):
    if len(m)==len(m[0]):
        print(f"Matrica je kvadratna")
    else:
        print("Matrica nije kvadratna")
print(is_square(m))
'''
#3. zadatak unos matrice
'''
def unos_matrice(redovi, kolone):
   
    matrica = []
    for i in range(redovi):
        red = []
        for j in range(kolone):
            vrednost = int(input(f'Unesite element [{i}][{j}]: '))
            red.append(vrednost)
        matrica.append(red)
    return matrica
print(unos_matrice(4,4)) 
'''
#4. zadatak -sabiranje matrica
'''
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[-1,-2,-3],[-4,-5,-6],[-7,-8,-9]]
C = []
def add(A,B):
    for i in range (len(A)):
        red=[]
        for j in range (len(A[0])):
            red.append(0)
        C.append(red)

    for i in range(len(A)):
        for j in range (len(A[0])):
            C[i][j]=A[i][j]+B[i][j]
    print(C)

print(add(A,B))
'''
#5. zadatak -transponovanje matrice, obrnuta matrica
'''
def transponuj_matricu(matrica):
    transponovana = []
    for j in range(len(matrica[0])):
        red = []
        for i in range(len(matrica)):
            red.append(matrica[i][j])
        transponovana.append(red)
    return transponovana
matrica=[[1,2],[3,4]]
print(transponuj_matricu(matrica))
'''
#6.zadatak -inverzovanje boja
'''
m=[[255,255,255],[0,0,0]]
def inverzna(matrica):
    nova=[]
    for i in range(len(matrica)):
        red=[]
        for j in range(len(matrica[0])):
            if matrica[i][j]==0:
                red.append(255)
            else:
                red.append(0)
        nova.append(red)
    return (nova)
print(inverzna(m))
'''
#7.zadatak 
'''
def check_matrix(A, string):
    rezultat = []
    for red in A:
        red_str = ''.join(red)         
        rezultat.append(red_str.count(string))  
    return rezultat
matrica = [["a", "b", "b", "a"],
           ["a", "c", "c", "a"],
           ["b", "a", "b", "a"],
           ["a", "b", "a", "f"]]

print(check_matrix(matrica, "ba"))
'''
#8. zadatak -broj neparnih elemenata iz parnih kolona
'''
def matrix_even(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(1, len(matrix[0]), 2):
            if matrix[i][j] % 2 != 0:
                count += 1
    return count
matrix= [[1, 5, 4], [3, 2, 2], [7, 5, 1]]
print(matrix_even(matrix))
'''
    



    



