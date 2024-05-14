#elenco docenti di una data classe

#funzione
def docenti_lezione(ora,giorno):
    giorni = ('lun','mar','mer','gio','ven')
    file = open('OrarioTabellaGlobale.csv','r') #apertura file in modalità lettura
    campi = next(file)
    ore = next(file)
    elenco = []
    if giorno in giorni:
        numero_iniziale = 5*giorni.index(giorno)
    else:
        print('Errore')
    cell = numero_iniziale + ora #posizione dell'elemento da scansionare
    for row in file: #scansione
        row = row.split(',')
        try:
            if  '  ' in row[cell]: #se la cella è vuota il docente non ha lezione
                continue
            else:
                nome_docente = row.pop(0)
                elenco.append(nome_docente)
        except IndexError: #quando il valore della variabile 'cell' arriva ad essere maggiore dell'indice della lista
            continue
    file.close() #chiusura file
    return elenco

while True: #loop infinito
    #input utente
    in_ora = int(input('Inserire ora scelta: '))
    in_giorno = input('Inserire le prime 3 lettere del giorno scelto: ').lower()
    
    #chiamata funzione
    docenti = docenti_lezione(in_ora, in_giorno)

    #stampa risultato
    print(f'I docenti che hanno lezione alla {in_ora} ora il {in_giorno} sono:')
    for elem in docenti:
        print(elem)

