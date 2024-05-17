from random import choice

your_name = input("Qual o seu nome?: ")
your_age = int(input("Sua idade: "))
your_job = input("Onde você trabalha?: ")

possibilites = [f'Um grande guerreiro chamando {your_name}, que possui {str(your_age)} anos de experiencia em suas costas, trabalhando de {your_job}, em uma vila muito distante.', f'Um jovem chamado {your_name} da cidade mais conhecida do mundo, com {str(your_age)} anos de idade, e trabalhando em uma enorme empresa como {your_job}']

print(choice(possibilites))