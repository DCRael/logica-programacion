'''Anagrama
Escribe una función que reciba dos palabras (STRING), las compare entre sí , retorne TRUE si es un anagrama y FALSE si no lo es.
Información adicional
Un Anagrama cosiste en formar una palabra reordenando TODAS las letras de otra palabra.
Ejemplo = Roma y Mora, Lacteo y Coleta,  Cara y Arca.
No hace falta comprobar que ambas palabras existan.
Dos palabras exactamente iguales NO SON un Anagrama.'''

def ver_anagrama(texto1,texto2):
    
    palabra1 = sorted(texto1)
    palabra2 =  sorted(texto2)

    return palabra1==palabra2

palabra1 = input('Ingresa la palabra2: ')
palabra2= input('Ingresa la palabra1: ')

if palabra1 == palabra2:
    print('no es anagrama')
else:
    r = ver_anagrama(palabra1,palabra2)

    if r:
        print('es anagrama')
    else:
        print('no es anagrama')
