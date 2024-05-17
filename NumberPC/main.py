from random import randint
import time

list_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

min_number = 0
max_number = list_numbers[-1]

rounds_game = 0
rounds_limit = 5

your_number = 0

def ver_PC(n, pc, r, l, li):
    if pc == n and not r == l:
        print(f'{str(r)}/{str(l)} - {str(pc)} ACERTOU')
        
    elif not pc == n and not r == (l + 1):
        print(f'{str(r)}/{str(l)} - {str(pc)} ERROU')
        li.remove(pc)
        if not r == 5:
            PC(n, r, l, li) 
        


def PC(n, r, l, li):
    pc_number = li[randint(0, len(li) - 1)]
    time.sleep(1)
    r += 1
    if r < (l + 1):
        ver_PC(n, pc_number, r, l, li)
    
    pass

def ver_n(n, r, l, li):
    while True:
        if n > min_number and n < max_number:
            break
        else:
            print(f'O Valor deve estar entre {str(min_number)} e {str(max_number)}')
            n = int(input(f'[{str(min_number)}/{str(max_number)}] Escolha um numero entre esse dois valores: '))
            
    PC(n, r, l, li)


def begin(n, r, l, li):
    n = int(input(f'[{str(min_number)}/{str(max_number)}] Escolha um numero entre esse dois valores: '))
    ver_n(n, r, l, li)

begin(your_number, rounds_game, rounds_limit, list_numbers)

