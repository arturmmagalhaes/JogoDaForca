#  -*- coding: utf-8 -*-

import random

lista_Erros = []
lista_Acertos = []
board = [
"""
 +---+
 |   | 
     |
     |
     |
=======
""",
""" 
 +---+
 |   | 
 O   |
     |
     |
=======
""",
""" 
 +---+
 |   | 
 O   |
 |   |
     |
=======
""",
""" 
 +---+
 |   | 
 O   |
/|   |
     |
=======
""",
""" 
 +---+
 |   | 
 O   |
/|\  |
     |
=======
""",
""" 
 +---+
 |   | 
 O   |
/|\  |
/    |
=======
""",
""" 
 +---+
 |   | 
 O   |
/|\  |
/ \  |
=======
"""
]

class Hangman:
    def __init__(self, word):
        self.word = word

    def guess(self, letter, quantidadeErros):
        contador = 0

        if letter not in lista_Acertos:
            for i in self.word:
                if i == letter:
                    contador += 1
                    lista_Acertos.append(letter)
            if contador == 0:
                quantidadeErros += 1
                lista_Erros.append(letter)
                print(lista_Erros)

        if quantidadeErros == 6:
            self.hangman_over()
        else:
            if len(lista_Acertos) == len(self.word):
                self.hangman_won()
            else:
                self.print_game_status(quantidadeErros)

    def hangman_over(self):
        print(board[6])
        print("\nGame over! Você perdeu.")
        print("A palavra era " + str(self.word))

    def hangman_won(self):
        print(self.word)
        print("Parabéns! Você venceu.")

    def hide_word(self):
        lista = ""

        for aux in self.word:
            if aux not in lista_Acertos:
                lista += "_"
            else:
                lista += aux

        print(lista)

    def print_game_status(self, quantidadeErros):
        print(board[quantidadeErros])
        self.hide_word()
        char = input("Digite uma letra: ")
        self.guess(char, quantidadeErros)

def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank)-1)].strip()

def main():
    global quantidadeErros
    quantidadeErros = 0

    game = Hangman(rand_word())
    game.print_game_status(quantidadeErros)

#    if game.hangman_won():

#    else:
#        print("\nGame over! Você perdeu.")
        #print("A palavra era " +Hangman.word)

if __name__ == "__main__":
    main()