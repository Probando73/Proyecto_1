from random import randrange

palabras = ["Ventilador", "Televisor", "Sillon"]

selector = randrange(0, len(palabras))

palabra_seleccionada = palabras[selector]

longitud_palabra = len(palabra_seleccionada)

remplazos = int(longitud_palabra*0.6)

text = palabra_seleccionada

for x in range(remplazos):

    modificacion = text.replace(
        palabra_seleccionada[randrange(0, longitud_palabra)], "_")
    text = modificacion

print(text)
