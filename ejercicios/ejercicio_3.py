import argparse
import sys
import os

#3- Escribir un programa en Python que acepte argumentos de línea de comando para leer un archivo de texto. 
#El programa debe contar el número de palabras y líneas del archivo e imprimirlas en la salida estándar. 
#Además el programa debe aceptar una opción para imprimir la longitud promedio de las palabras del archivo. 
#Esta última opción no debe ser obligatoria. Si hubiese errores deben guardarse el un archivo cuyo nombre será "errors.log" usando la redirección de la salida de error.
def main():   
    parser = argparse.ArgumentParser()
    parser.add_argument('archivo', type=str, help='escribir la ruta al archivo de texto')
    args = parser.parse_args()

    try:
        with open(args.archivo, 'r') as archivo:
            contenido = archivo.read()
            palabras = contenido.split()
            cantidad_palabras = len(palabras)
            lineas = contenido.split('\n')
            cantidad_lineas = len(lineas)
        print('El archivo', args.archivo, 'tiene', cantidad_palabras, 'palabras y', cantidad_lineas, 'líneas.')     
    except FileNotFoundError:
        with open("errors.log", "a") as error_file:
            error_file.write("The file {} does not exist\n".format(args.archivo))
        sys.stderr.write("The file {} does not exist\n".format(args.archivo))
        sys.exit(1)

if __name__ == "__main__":
    main()
