#!/usr/bin/python3

def factors(num):
    lista = []
    for i in range(num):
        for j in range(num):
            if num == i * j and i not in lista:
                lista.append(i)
                lista.append(j)
    print("{:d} = {:d}*{:d}".format(num, lista[0], lista[1], end='\n'))
                          

def main():
    with open("file.txt") as f:
        for num in f:
            factors(num.strip())

