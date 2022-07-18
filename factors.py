#!/usr/bin/python3
import sys

def factors(num):
    num = int(num)
    if num % 2 == 0:
       print("{:d} = {:d}*2".format(num, num//2))
    else:
        for item in range(3, num, 2):
            if num % item == 0:
                quotient = num//item   
                print("{:d} = {:d}*{:d}".format(num, quotient, item))
                break

def sortfile(file=sys.argv[1]):
    inp_file = open(file, "r")
    integers = []
    for k in inp_file:
        integers += k.strip().split()
    inp_file.close()
    integers = map(int, integers)
    tigers = list(integers)
    tigers.sort()
    tigers = map(str, tigers)
    tigers = list(tigers)
    out_file = open("result", "w")
    for j in tigers:
        out_file.writelines(j)
        out_file.writelines('\n')
    out_file.close()

def main():
    filey = sortfile(sys.argv[1])
    with open("result") as f:
        for num in f:
            numz = int(num[:-1])
            factors(numz)

if __name__ == "__main__" :
    main()
