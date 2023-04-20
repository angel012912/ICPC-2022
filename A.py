from tkinter.messagebox import RETRY
from typing import Optional


import time 

# def count_monotonicy(cadena: str, prev: str) -> int:
#     if len(cadena) == 0:
#         return 0
#     c = count_monotonicy(cadena[1:], cadena[0])
#     if prev == 'a' and (cadena[0] == 'a' or cadena[1] == 'a'):
#         return c + 1
#     return c

# def check_monotonicy(character: str) -> int :
#     r = count_monotonicy(character[1:], character[0])
#     return r

# def check_monotonicy(character: str) -> int: 
#     counter = 0
#     res = 0
#     while counter < len(character):
#         if character[counter] == 'a':
#             if ((counter + 1 < len(character) and character[counter + 1] == 'a') or (counter - 1 >= 0 and character[counter - 1] == 'a')):
#                 res += 1
#         counter += 1
#     return res

def check_monotonicy(cadena: str) -> int:
    counter = 0
    res = 0
    length = len(character)
    while counter < length:
        if character[counter] == 'a':
            if ((counter + 1 < length and character[counter + 1] == 'a') or (counter - 1 >= 0 and character[counter - 1] == 'a')):
                res += 1
        counter += 1
    return res

if __name__ == '__main__':
    number = int(input())
    character = str(input())
    if (1 <= number <= 10**5 and len(character) == number):
        print(check_monotonicy(character))
