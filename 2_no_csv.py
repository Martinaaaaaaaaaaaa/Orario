#orario di un determinato docente e numero totale delle ore del docente

#funzione
def orario_docente(docente):
    file = open('OrarioTabellaGlobale.csv','r') #apertura file in modalità lettura
    #campi e ore vengono tirati fuori come liste così da non essere incluse nel ciclo di ricerca
    campi = next(file)
    ore = next(file)
    for row in file:
        if docente in row[0]:
            
    for elem in riga:
        if elem != '   ':
            cont += 1
    file.close() #chiusura file
    return campi, ore, riga, cont

#input utente
in_docente = 'ADAMOLI PAOLO' #input('Inserire il docente [tutto in maiuscolo]: ') 

#chiamata funzione
orario = orario_docente(in_docente)

#ho un problema con il print dell'orario

orario_stampa = orario[0],orario[1],orario[2] #non prendo in considerazione le ore totali
print(orario[0].pop(0).strip(), in_docente) #print nome docente


for elem in orario_stampa: #loop stampa
    if elem[].strip() != '':
        print(elem[x].strip(), ' ', end = '')
    else :
        print(elem[x+1])
    

#print ore totali
print(f'ore totali di {in_docente}: {orario[3]}')