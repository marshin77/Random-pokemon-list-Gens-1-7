import math
import random
from random import randint

def yieldlines(f):
    x = int(807)
    y = int(input("number of random Bokemon XD :"))
    lines=f.readlines()
    for i in range(y):
        print lines[randint(1,x)]
  

def hold ():
    z = raw_input("would like to stop?[y/n]:")
    if z.lower() in ['y','yes']:
        return
    elif z.lower() in ['n','no']:
        main()
        
    

def main():
    fp = open("file.txt")
    yieldlines(fp)
    hold()
    fp.close()
    exit()
    
main()
