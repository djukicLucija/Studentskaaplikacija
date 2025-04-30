'''l1=[10,20,30]
l2=[50,60,70]
l1=l2.copy()
l2[0]=100
print(l1,l2)
'''
'''
d={"ime":"Ana", "prezime":"Markovic", "godina_studija":2,"prosjek":8.5}
d["prosjek"]=9
print(d)
'''
'''
l=[1,1,2,2,3,3]
l1=list(set(l))
print(l1)'''

#Zadatak 1

lista_studenata=[{"ime":"Lucija","prezime":"Djukic","broj_indeksa":"23/016","godina_studija":2,"prosjek":9.8},
                 {"ime":"Arslan","prezime":"Vlahovljak","broj_indeksa":"23/006","godina_studija":1,"prosjek":9.4},
                 {"ime":"Marko","prezime":"Maric","broj_indeksa":"23/116","godina_studija":1,"prosjek":9.3},
                 {"ime":"Matija","prezime":"Maric","broj_indeksa":"23/055","godina_studija":3,"prosjek":9.8}
]

ukupno=0
br_studenata=0
for student in lista_studenata:
    if student["godina_studija"]==1:
        ukupno+=student["prosjek"]
        br_studenata+=1
print(f"Prosjek studenata sa prve godine je "{ukupno/br_studenata})






