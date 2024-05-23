
def create_tabuada(number):
    n = 0
    while n < 10:
        n += 1
        res = number * n
        print(f'{str(number)} x {str(n)} = {str(res)}')


def set_operator(number):
    number = int(input("Tabuada de "))
    
    if not number > 10 and not number < 0:
        create_tabuada(number)


number = 0

set_operator(number)