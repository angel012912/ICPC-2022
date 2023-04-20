def check_monotonicy(character: str) -> int :
    counter: int = 0
    res: int = 0
    while character[counter] :
        if character[counter]  == 'a':
            counter += 1
            while(character[counter] == 'a'):
                res += 1
                counter += 1
    return counter
            


number: int = int(input())
character: str = str(input("Hola: "))
print(check_monotonicy(character))