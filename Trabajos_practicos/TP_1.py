
 

import os
import argparse
import sys 


parser = argparse.ArgumentParser()    
parser.add_argument('-f', '--file', type=str, help='Indicar el archivo de texto que se quiere utilizar.')
args= parser.parse_args()         



try:
    with open(args.file, "r") as archivo:
        lineas = archivo.readlines()
        numero_de_lineas = len(lineas)
    archivo.close()
except (FileNotFoundError, PermissionError):
    print("El archivo no existe o no se puede abrir.")
    exit()

archivo= []


for i in lineas:
    r_padre, w_hijo = os.pipe()
    r_hijo, w_padre = os.pipe()
    pid = os.fork()
    if pid == 0:
        os.close(r_padre)  
        os.close(w_padre)
        linea = os.read(r_hijo, 1024).decode()
        os.close(r_hijo)
        linea_invertida = linea[::-1]
        os.write(w_hijo, linea_invertida.encode())            
        os.close(w_hijo)
        sys.exit(0)
    else:
        os.close(r_hijo)
        os.close(w_hijo)
        lineas_2 = i.strip()
        os.write(w_padre, lineas_2.encode())
        os.close(w_padre)
        lineas_3 = os.read(r_padre, 1024).decode().strip()
        os.close(r_padre)
        archivo.append(lineas_3)

for x in archivo:
    print(x)