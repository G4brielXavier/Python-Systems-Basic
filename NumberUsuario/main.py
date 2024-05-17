from random import randint

min = 0
max = 10

number_computer = 0
max_limit = 5
rounds = 0

computer_n = randint(min, max)
number_client = int(input(f'Round {str(rounds)}/{str(max_limit)} - Adivinhe o numero: '))

while not number_client == computer_n and not rounds == max_limit:
    rounds += 1
    print(" ") 
    print("Errou")
    print(" ")     
    number_client = int(input(f'Round {str(rounds)}/{str(max_limit)} - Adivinhe o numero: '))
    
else:
    print(" ")    
    print("Acertou") 
    print(" ")   