#!/usr/bin/python3
import math

def prime_product(n):
    numz = math.floor(n/3)
    n_list = list(range(2, numz+1))
    primelist = [2,3,5,7]
    for item in n_list:
        if (item % 2 != 0 and item % 3 != 0 and item % 5 != 0 and item % 7 != 0):
            primelist.append(item)
    print(primelist)        
    comp = []
    i = 0
    while i <= len(primelist) and len(comp) < 2:
        for item in primelist:
            if primelist[i] * item == n:
                comp.append(primelist[i])
                comp.append(item)
        i = i+1
    print("{:d} = {:d}*{:d}".format(n, comp[1], comp[0], end='\n'))
            

def main():
    with open(sys.argv[1]) as f:
        for num in f:
            prime_product(int(num))

if __name__ == "__main__" :
    main()
