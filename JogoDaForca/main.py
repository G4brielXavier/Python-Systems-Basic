from random import choice

word_list = {
    "Words":["casa", "carro", "cachorro", "bola", "foguete"]
}

letters_space_list = []
line_letter = []
letters_no_correct = []

start_game = False

word_process = choice(word_list["Words"])

for i in word_process:
    letters_space_list.append(i)
    line_letter.append(" _ ")

print(letters_space_list)

word = f'| {line_letter}'

def ask(st, w):
    st = True
    letter = str(input("One Letter: ").lower())
    structure_forca(st, letter, w)

def structure_forca(st, letter, word):
    if st:
        for lett in letters_space_list:
            if lett == letter:
                line_letter[letters_space_list.index(lett)] = lett
                word = f'| {line_letter}'
            else:
                pass
        letters_no_correct.append(letter)
        
    print("              ")
    print("              ")
    print("              ")
    print(f'Letras Usadas: {letters_no_correct}')
    print("     Jogo da Forca     ")
    print("____")
    print("|  |")
    print("|  o")
    print("| |||")
    print("|  LL")
    print("|")
    print(word)
    print("              ")
    print("              ")
    print("              ")
    ask(start_game, word)
pass

structure_forca(start_game, "", word)
