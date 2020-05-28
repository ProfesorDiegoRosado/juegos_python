
import random
import copy


def remove_trailing_carriage_return(s):
    if s[-1]=="\n":
        return s[0:len(s)-1]
    else:
        return s

def load_words(filename):
    words = {}  # crea un diccionario vacio
    f = open(filename, "r")
    lines = f.readlines()
    for l in lines:
        splited = l.split(":")
        if len(splited)==2:
            word = splited[0]
            definition = remove_trailing_carriage_return(splited[1])
            words.update( {word: definition})
    return words

def get_random_word_definition(words):
    key_list = list(words)
    rand_pos = random.randint(0, len(key_list)-1)
    word = key_list[rand_pos]
    definition = words[word]
    return (word, definition)

def get_random_word(words):
    words_copy = copy.deepcopy(words)
    # Busca la palabra y la definicion
    (word, definition) = get_random_word_definition(words_copy)
    del words_copy[word]   # quita la palabra del diccionario de palabras temporales
    # Busca la definicion a falsa 1
    (ignore_word1, false_answer1) = get_random_word_definition(words_copy)
    del words_copy[ignore_word1]   # quita la palabra del diccionario de palabras temporales
    # Busca la definicion a falsa 2
    (ignore_word2, false_answer2) = get_random_word_definition(words_copy)
    del words_copy[ignore_word2]   # quita la palabra del diccionario de palabras temporales
    # Busca la definicion a falsa 3
    (ignore_word3, false_answer3) = get_random_word_definition(words_copy)
    del words_copy[ignore_word3]   # quita la palabra del diccionario de palabras temporales
    # devuelve los valores encontrados
    return (word, definition, false_answer1, false_answer2, false_answer3)

def show_word(word, answer, false_answer1, false_answer2, false_answer3):
    choices = {1: answer, 2: false_answer1, 3: false_answer2, 4: false_answer3}
    random_answers = {}
    right = 0
    for n in range(1, len(choices)+1):
        number = random.choice(list(choices))
        random_answers.update( { n: choices[number] } )
        del choices[number]
        if number == 1:
            right = n
    print("¿Cuál es la definición de la palabra \"" + word + "\"?")
    for k,v in random_answers.items():
        print(str(k) + ".- " + v)   # muestra numero y respuesta
    return right

def read_option():
    option = input("Introduzca la opción de respuesta que usted decida (0 para salir): ")
    if '0' <= option and option <= '4':
        return int(option)
    else:
        print(" - opción incorrectar - ")
        return read_option()


end = False

filename = input("Introduzca el nombre del archivo diccionario: ")
words = load_words(filename)
aciertos = 0
errores = 0

while not end:
    (word, answer, false_answer1, false_answer2, false_answer3) = get_random_word(words)
    right_number = show_word(word, answer, false_answer1, false_answer2, false_answer3)
    option = read_option()
    # comprueba si la opcion es salir
    if option == 0:
        end = True
    else:   # Si no es salir, vemos si has acertado o no
        if right_number == option:
            print("Has acertado!!\n")
            aciertos = aciertos + 1
        else:
            print("Te has equivocado\n")
            errores = errores + 1

# Mostramos un resumen del juego
print("\n"*2)
print("Resumen de la partida:")
print("======================")
print("En este partida has jugado " + str(aciertos+errores) + " palabras")
print("Has acertado " + str(aciertos) + " palabras")
print("Has cometido " + str(errores) + " errores")
