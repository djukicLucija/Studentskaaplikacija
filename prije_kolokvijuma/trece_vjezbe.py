'''
#1. zadatak
predmeti=[{"ime":"Puzle","tezina":50,"vrijednost":40},
          {"ime":"autic","tezina":30,"vrijednost":42},
          {"ime":"markeri","tezina":10,"vrijednost":50}]

def ukupna_tezina(predmeti):
    ukupna_tezina=0
    for predmet in predmeti:
        ukupna_tezina+=predmet["tezina"]
    return ukupna_tezina
print(ukupna_tezina(predmeti))

def najvrijedniji_predmet(predmeti):
    najvrijedniji_predmet=predmeti[0]
    for predmet in predmeti:
        if predmet["vrijednost"]>najvrijedniji_predmet["vrijednost"]:
            najvrijedniji_predmet=predmet
    return najvrijedniji_predmet["ime"]
print(najvrijedniji_predmet(predmeti))
'''
'''
#2 zadatak
 zadati=[{"naziv":"prvi","status":"zarvsen","nagrada":"1 bod"},
          {"naziv":"drugi","status":"neodradjen","nagrada":"2 boda"},
          {"naziv":"treci","status":"neodradjen","nagrada":"3 boda"},]

def mijenjanje_statusa (zadati, naziv):
 zadatak1="drugi"
 for zadatak in zadati:
  if zadati["naziv"]== naziv:
   zadatak["status"]="zavrsen"
 return zadati
print(zadati)
 def ukupna_narada (zadati):
nagrada=0
for zadatak in zadati:
    if zadati["status"]=="zavrsen":
      nagrada+=zadati["nagrada"]
return nagrada

print(ukupna_nagrada(zadati))
'''

 
