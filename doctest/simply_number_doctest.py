from os import system
system('cls')
import doctest

def simply_number(number: int):
    """
    >>> simply_number(11)
    True
    
    >>> simply_number(100)
    False

    >>> simply_number(1000)
    False
    """
    
    current = 2
    count = 0
    while current < number:
        if number % current == 0:
            count += 1
        current += 1
    if count != 0 or number == 0 or number == 1:
        return False
    else:
        return True    

if __name__ == "__main__":
    # num = int(input('Введите положительное число: \n' ))
    # print(simply_number(num))
    doctest.testmod(verbose=True)