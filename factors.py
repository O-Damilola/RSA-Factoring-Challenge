#!/usr/bin/python3

import sys

def factors(num):
    lista = []
    for i in range(num):
        for j in range(num):
            if num == i * j and i not in lista:
                lista.append(i)
                lista.append(j)
    print("{:d} = {:d}*{:d}".format(num, lista[1], lista[0], end='\n'))



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
