from random import choice

list_options = ["Rock", "Paper", "Scissor"]

def computer_chose(your_opt):
    pc_opt = choice(list_options)

    if your_opt == "Rock" and pc_opt == "Scissor" or your_opt == "Paper" and pc_opt == "Rock" or your_opt == "Scissor" and pc_opt == "Paper":
        print(f'You: {your_opt} win PC: {pc_opt}')
    elif pc_opt == "Rock" and your_opt == "Scissor" or pc_opt == "Paper" and your_opt == "Rock" or pc_opt == "Scissor" and your_opt == "Paper":
        print(f'PC: {pc_opt} lose  You: {your_opt}')
    elif your_opt == pc_opt:
        print("Draw")

def verify_option(opt):
    while True:
        if opt in ["Rock", "Paper", "Scissor"]:
            computer_chose(opt)
            break
        else:
            opt = str(input("Rock, Paper or Scissor?: ").capitalize())
            verify_option(opt)

def begin():
    option = str(input("Rock, Paper or Scissor?: ").capitalize())
    verify_option(option)
    
begin()