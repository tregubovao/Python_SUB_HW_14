from os import system
system('cls')

def simp_num(number: int):
   
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
    print(simp_num(13))