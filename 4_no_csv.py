#elenco docenti di una data classe

#funzione
def docenti_lezione(ora,giorno):
    file = open('OrarioTabellaGlobale.csv','r') #apertura file in modalità lettura
    campi = next(file)
    ore = next(file)
    for row in file:
        row = row.split(',')
        nome = row.pop(0)
        
    file.close() #chiusura file
    return elenco

while True: #loop infinito
    #input utente
    in_ora = int(input('Inserire ora scelta: '))
    in_giorno = input('Inserire prime 2 lettere del giorno scelto: ')
    
    #chiamata funzione
    docenti = docenti_lezione(in_ora, in_giorno)

    #stampa risultato
    print(f'I docenti che hanno lezione alla {in_ora} ora il {in_giorno} sono: \n')
    for elem in docenti:
        print(elem)

