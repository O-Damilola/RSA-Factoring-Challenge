#!/usr/bin/python3

import sys

def prime_product(n):
    """ Prints the prime product of a number"""
    if n % 2 == 0:
            print("{}={}*2".format(n, n//2))
    else:
        for value in range(3, n, 2):
            if n % value == 0:
                quotient = n//value
                for valz in range(3, quotient, 2):
                    if quotient % valz == 0 or value % valz == 0:
                        break
                print("{}={}*{}".format(n, quotient, value))
                break
   
def main():
    """ Carries out the prime product process"""
    with open(sys.argv[1]) as book:
        for num in book:
            prime_product(int(num))

if __name__ == "__main__" :
    main()

