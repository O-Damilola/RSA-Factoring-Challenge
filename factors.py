#!/usr/bin/python3

import sys

def factors(num):
    numz = (num//2) + 1
    if num % 2 == 0:
       print("{:d} = {:d}*2".format(num, num//2))
    else:
        for item in range(3, numz+2, 2):
            if num % item == 0:
                quotient = num // item   
                print("{:d} = {:d}*{:d}".format(num, quotient, item))
                break

def sortfile(file=sys.argv[1]):
    inp_file = open(file)
    integers = []
    for line in inp_file:
        integers.append(int(line))
    inp_file.close()
    integers.sort()
    integers = map(str, integers)
    integers = list(integers)
    out_file = open("result", "w")
    for j in integers:
        out_file.writelines(j)
        out_file.writelines('\n')
    out_file.close

def main():
    filey = sortfile(sys.argv[1])
    with open("result") as f:
        for num in f:
            factors(int(num))

if __name__ == "__main__" :
    main()
