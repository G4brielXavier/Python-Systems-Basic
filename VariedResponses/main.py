from random import randint

def begin():
    inpt = str(input("IA - What's your name: "))
    return inpt

name = begin()
respost = ["Como vai?", "Como posso ajudar?", "Prazer em te conhecer", "Como está?"]
initial = ["Ola", "Oi", "Eai", "Beleza"]

print(f'IA - {initial[randint(0, len(initial))]} {name}, {respost[randint(0, len(respost))]}')