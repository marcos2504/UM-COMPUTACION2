import getopt
import sys

(opts, args) = getopt.getopt(sys.argv[1:], "n:")
for (o,a) in opts:
    if o == "-n":
        n= int(a)
        i=[]
        for x in range (n*2):
            if x%2 == 1:
                i.append(x)
        print(i)