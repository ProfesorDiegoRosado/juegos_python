



def hangman0():
    print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')

def hangman1():
    print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')

def hangman2():
    print('''
  +---+
  |   |
  O   |
      |
      |
      |
=========''')

def hangman3():
    print('''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''')

def hangman4():
    print('''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''')


def hangman5():
    print('''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''')

def hangman6():
    print('''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''')


def hangman7():
    print('''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')

def show_hangman(mistakes):
    if mistakes==0:
        hangman0()
    elif mistakes==1:
        hangman1()
    elif mistakes==2:
        hangman2()
    elif mistakes==3:
        hangman3()
    elif mistakes==4:
        hangman4()
    elif mistakes==5:
        hangman5()
    elif mistakes==6:
        hangman6()
    else:  # sabemos que si llegamos aquí solo pueden ser 7 errores
        hangman7()

def clear_screen():
    print("\n"*80)

def show_word(word, letters):
    for c in word:
        if c in letters: # la letra está en las letras que hemos dicho
            print(c, end="")
        else:   # la letra NO está en las letras que hemos dicho
            print("_", end="")   # imprimimos un hueco para que no se vea que letra es
        print(" ", end="")   # en cualquier de los dos casos imprimimos un espacio para separar cada letra de la anterior
    print()    # Cuando termino de mostrar la palabra escribo un retorno de carro para escribir en la siguiente linea

def word_guessed(word, letters):
    guessed = True
    for c in word:
        if c not in letters:
            guessed = False
    return guessed


hidden_word = input("Introduzca la palabra a adivinar: ")
clear_screen()

end = False
mistakes = 0
letters = set()    # conjunto con las letras que hemos dicho para adivinar la palabra escondida

while not end:
    show_hangman(mistakes)
    show_word(hidden_word, letters)

    letter = input("Introduzca una letra: ")
    letters.add(letter)     # añadimos la letra que hemos leido al conjunto
    if letter in hidden_word:   # Si la letra está en la palabra oculta
        print("Bien, has acertado una letra.")
    else:   # la letra no está en la palabra oculta
        print("Error, la letra " + letter + " no está en la palabra oculta.")
        mistakes = mistakes + 1

    end = mistakes == 7 or word_guessed(hidden_word, letters)
    print()   # Imprimimos una linea vacia para separar un poco un turno del siguiente

# El juego puede acabar por dos motivos, o por llegar al numero de errores o porque has acertado la palabra
if mistakes == 7:  # Si acaba por numero de errores
    print("Has muerto ahorcado por no tener vocabulario.")
else:   # Si acaba porque sabes la palabra
    print("Bien, has hacertado la palabra oculta.")
    print("La palabra oculta era: " + hidden_word)
