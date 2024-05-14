#orario di un determinato docente e numero totale delle ore del docente

#funzione
def disposizione_docente(docente):
    file = open('OrarioTabellaGlobale.csv','r') #apertura file in modalità lettura
    #campi e ore vengono tirati fuori come liste così da non essere incluse nel ciclo di ricerca
    campi = next(file)
    ore = next(file)
    for row in file:
        if docente in row: #prende in considerazione solo la riga che contiene il nome del docente
            cont = 0 #contatore per ore a disposizione
            for ora in row:
                if ora == 'D': #evita di prendere in considerazione le cassi che hanno D dentro mettendo uno spazio davanti
                    cont += 1
            disposizione = [docente,cont]  #lista con nome docente e ore a disposizione
            break #evita che vengano prese in considerazione altre righe inutilmente
    file.close() #chiusura file
    return disposizione

while True: #loop infinito
    #input utente
    in_docente = input('Inserire il docente desiderato: ').upper()

    #chiamata funzione
    disp = disposizione_docente(in_docente)

    #stampa risultato
    print(disp[0] + "\nOre a disposizione: " + str(disp[1]) )

