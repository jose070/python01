

def buscar(indice, lista):
    cadena = [lista[indice]]
    cont = 0
    while (cont < len(lista)):
    	if not (lista[cont] in cadena) and lista[palabra].endswith(lista[cont][0]):
    		indice=cont
    		cadena = [lista[cont]]+1
    		cont = 0
    	cont = cont + 1
    return cadena
    

    fichero = open(pokemon.txt) 
    texto =fichero.read()
    fichero.close()
    texto = texto.replace('\n',' ')
    texto = texto.split(' ')
    cadenapal = texto[0]
    for cont in range(len(texto)):
        cad = buscar(cont,texto)
        if len(cad)>len(cadenapal):
        	cadenapal= cad
    print "la cadena mas larga es"
    print cadenapal
    print "y su longitud es" 
    print len(cadenapal)








j