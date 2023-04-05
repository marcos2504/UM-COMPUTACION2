#Realizar un programa que implemente fork junto con el parseo de argumentos. 
#Deberá realizar relizar un fork si -f aparece entre las opciones al ejecutar el programa. 
#El proceso padre deberá calcular la raiz cuadrada positiva de un numero y el hijo la raiz negativa.
import argparse
import os
import numpy
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-n","--number", help="elije un numero para sacarle la raiz", type=int)
parser.add_argument("-f","--fork", help="proceso fork", action="store_true")
args = parser.parse_args()

if  args.fork == True :
    pid = os.fork()
    if pid > 0:
        r= numpy.sqrt(args.number)
        p= os.getpid()
        print( f'Soy el proceso padre \n PID {p} \n La raiz cuadrada es {r} ')
    elif pid == 0 :
        r=r= numpy.sqrt(args.number)
        p= os.getpid() 
        print( f'Soy el proceso hijo  \n PID {p} \n La raiz cuadrada negativa  es {-r} ')

else:
    r= numpy.sqrt(args.number)
    p= os.getpid()
    print( f'Soy el proceso padre \n PID {p} \n La raiz cuadrada es {r} ')




