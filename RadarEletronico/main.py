from time import sleep
from random import randint, choice 
import pandas as pd



km_traffic = [40, 60, 80, 100]
carros = ["Tesla Model Y", "Tesla Model X", "BYD Dolphin", "BYD Mini", "BYD Seal", "BYD Yuan", "BYD Han", "BYD Shark", "Corvete", "Lamborghini", "Ferrari", "Supra Mk4", "Supra Mk5", "Nissan GTR-35"]

carros_table = {
    "Carros":[],
    "Multa":[],
}

time_cars_pass = 0
carros_number = 0
carro_name = ""
km = 0
tax = "Não"
km_limit = choice(km_traffic)
cars = 0
cars_total = randint(2, 8)

def pass_car():    
    global time_cars_pass, carro_name, carros_number, km
    
    time_cars_pass = randint(1, 4)
    carros_number = randint(0, len(carros))
    carro_name = carros[carros_number]
    km = randint(40, 300)
    
def ver_km_car():
    global km, km_limit, tax
    
    if km >= km_limit:
        tax = "Sim"
    else:
        tax = "Não"
       
def set_in_table(model, tax):
    carros_table["Carros"].append(model)
    carros_table["Multa"].append(tax)
 
print(f'Velocidade Limite da Vía é {str(km_limit)}')
print(" ")

while cars < cars_total:
    sleep(time_cars_pass)
    cars += 1
    pass_car()
    ver_km_car()
    
    set_in_table(carro_name, tax)
    
    print(" ")
    print(f'Opa! \n Modelo: {carro_name} \n Velocidade: {str(km)}Km/h \n Multa?: {tax}')
    print(" ")
    

data_cars = pd.DataFrame(carros_table)
print(data_cars)
print(" ")





