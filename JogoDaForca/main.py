from random import choice

word_list = ["cachorro", "gato", "vaca", "macaco", "elefante", "coelho", "abelha", "sapo", "leão", "onça", "guaxinim", "leopardo", "rinoceronte", "formiga", "mosca", "salamandra", "rato", "ovelha", "cabra", "boi"] # lista de palavras disponiveis no sistema

letters_used = [] # letras que foram usadas mais não são as corretas

start_game = False # controlador de inicio de processo

word_process = choice(word_list) # palavra escolhida e armazenada na variavel
line_letter = [ '_' for _ in word_process ] # linhas que representam cada letra da palavra escolhida
letters_space_list = list(word_process) # lista que armazena cada letra da palavra escolhida

word = f'| {line_letter}'

head = ""
left_arm = ""
body = ""
right_arm = ""
left_foot = ""
right_foot = ""

life = 0

def build_character(l):
    global head, body, left_arm, right_arm, left_foot, right_foot
    
    if l == 1:
        head = "o"
    
    if l == 2:
        body = "|"
    
    if l == 3:
        left_arm = "|"
        
    if l == 4:
        right_arm = "|"
        
    if l == 5:
        left_foot = "L"
    
    if l == 6:
        right_foot = "L"
        
    pass

def ask(st, w, lif, ctrl):
    ctrl = True
    letter = input("Adivinhe a letra: ").lower()
    
    
    if not letter in letters_space_list or not letter == word_process:
        lif += 1
        build_character(lif)
        
        
    if letter == word_process:
        con_list = list(letter)
        for indx, lett in enumerate(con_list):
            line_letter[indx] = lett
            w = f'| {line_letter}'
        st = False
        ctrl = True
        structure_forca(st, letter, w, lif, ctrl)
    else:
        st = True
        ctrl = True
        structure_forca(st, letter, w, lif, ctrl)


def structure_forca(st, letter, word, lif, ctrl):
    no_lett = ""
    
    if st:
        for indx, lett in enumerate(letters_space_list):
            if ctrl:
                if lett == letter:
                    line_letter[indx] = lett
                    word = f'| {line_letter}'
    
    
                    
                
    letters_used.append(letter)
        
    print("              ")
    print("              ")
    print("              ")
    print(f'Letras Usadas: {letters_used}')
    print("     Jogo da Forca     ")
    print("____")
    print("|  |")
    print(f'|   {head}')
    print(f'| {left_arm}{body}{right_arm}')
    print(f'| {left_foot}{right_foot}')
    print("|")
    print(word)
    print("              ")
    print("              ")
    print("              ")
    if lif < 6:
        ask(start_game, word, lif, ctrl)
    else:
        print(f'Sem Chances! \n A Palavra era {str(word_process)}')
pass

control = False

structure_forca(start_game, "", word, life, control)
