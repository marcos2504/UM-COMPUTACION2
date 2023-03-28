import getopt
import sys
#Escribir un programa en Python que acepte dos argumentos de línea de comando: una cadena de texto, un número entero. 
#El programa debe imprimir una repetición de la cadena de texto tantas veces como el número entero.
(opts, args) = getopt.getopt(sys.argv[1:], "t:n:", ["texto=","numero="])
t=''
n=''
for (o,a) in opts:
    if o in ("-t", "--texto"):
        t=(str(a)+'\n')
    if o in ("-n", "--numero"):
        n= int(a)
print( (t * n ))