
with open('cambio.txt', 'r') as archivo:
    contenido = archivo.read()
    #print(contenido)
    
import pandas as pd
with open('cambio2.txt', 'r') as archivo:

    df = pd.read_csv('cambio2.txt', delimiter='\t')
    print(df+contenido+"feature3")

with open('cambiob.txt', 'r') as archivo:
    contenidob = archivo.read()
    print(contenidob)
    ##listo release
    ##listo pull main
