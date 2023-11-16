
with open('cambio.txt', 'r') as archivo:
    contenido = archivo.read()
    print(contenido)
    
import pandas as pd
with open('cambio2.txt', 'r') as archivo:

    df = pd.read_csv('cambio2.txt', delimiter='\t')
    print(df)
