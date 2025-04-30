matrica=[[1,2,3],[4,5,6],[7,8,9]]

br_redova=3
br_kolona=3
for i in range(br_redova):
    for j in range (br_kolona):
        if matrica[i][j]%2==0:
            matrica[i][j]=matrica[i][j]**2
print(matrica)
