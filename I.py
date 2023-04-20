if __name__ == '__main__':
    numeros = str(input())
    numeros = [int(x) for x in numeros.split()]
    numeros = set(numeros)
    if 9 in numeros:
        print("F")
    else:
        print("S")