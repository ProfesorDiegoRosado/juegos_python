# Author: Profesor Diego Rosado
# Battleships game python implementation


# https://misc.flogisoft.com/bash/tip_colors_and_formatting
BLINK = "\033[33;5m"
YELLOW = "\033[33"
BLUE = "\033[34m"
LIGHT_GRAY = "\033[37m"
NORMAL = "\033[0m"

BG_BLUE = "\033[104m"
BG_YELLOW = "\033[103m"


UNKNOWN: chr = '□'
BATTLESHIP: chr = 'o'
WATER: chr = '~'
HIT: chr = '#'


class Board:

    def __init__(self):
        # Tablero con la información completa de los barcos y el agua
        self.hidden_board = [
            #1           2           3           4           5           6           7           8
            [WATER,      WATER,      WATER,      WATER,      WATER,      WATER,      WATER,      WATER],  # a
            [WATER,      WATER,      WATER,      WATER,      WATER,      WATER,      WATER,      WATER],  # b
            [WATER,      WATER,      WATER,      WATER,      WATER,      WATER,      WATER,      WATER],  # c
            [BATTLESHIP, WATER,      WATER,      WATER,      WATER,      WATER,      WATER,      WATER],  # d
            [BATTLESHIP, WATER,      WATER,      WATER,      WATER,      WATER,      WATER,      WATER],  # e
            [WATER,      WATER,      WATER,      WATER,      WATER,      WATER,      WATER,      WATER],  # f
            [WATER,      WATER,      WATER,      WATER,      WATER,      WATER,      WATER,      WATER],  # g
            [WATER,      WATER,      WATER,      WATER,      WATER,      WATER,      WATER,      WATER]   # h
        ]
        # Tablero con la información actual del juego. Se inicializa todo a casillas desconocidas (UNKNOWKN)
        self.board = [[UNKNOWN for row in range(len(self.hidden_board))] for column in range(len(self.hidden_board[0]))]

    def draw(self):
        print("  1 2 3 4 5 6 7 8")
        for i in range(len(self.board)):
            row = self.board[i]
            print(chr(ord('a')+i) + " ", end="")
            for j in range(len(row)):
                tile = row[j]
                print(tile + " ", end="")
            print()

    def draw_cool(self, turn: (int,int)):
        print("  1 2 3 4 5 6 7 8")
        for i in range(len(self.board)):
            row = self.board[i]
            print(chr(ord('a')+i) + " ", end="")
            for j in range(len(row)):
                tile = row[j]
                if i == turn[0] and j == turn[1]:
                    print(YELLOW, end="")
                elif tile == WATER:
                    print(BLUE, end="")
                    print(BG_BLUE, end="")
                elif tile == HIT:
                    print(LIGHT_GRAY, end="")
                print(tile + " ", end="")
                print(NORMAL, end="")
                #print(" x: " + str(i) + " , j: " + str(j), end="")
            print()

    def check(self, turn: (int, int)):
        row = turn[0]
        column = turn[1]
        spot = self.hidden_board[row][column]
        if spot == WATER:
            self.board[row][column] = WATER
            return WATER
        else:  # spot==BATTLESHIP
            self.board[row][column] = HIT
            return HIT

    def count(self, board, symbol):
        count = 0
        for i in range(len(board)):
            row = board[i]
            for j in range(len(row)):
                element = row[j]
                if element == symbol:
                    count = count + 1
        return count

    def check_end(self):
        battleships = self.count(self.hidden_board, BATTLESHIP)
        hits = self.count(self.board, HIT)
        return battleships == hits


class Player:

    def __init__(self):
        pass

    def read_row(self):
        row = input("Introduce una letra (entre a y h): ")
        if 'a' <= row <= 'h':
            row = ord(row) - ord('a')
        else:
            print("Introduzca una letra entre la a y la h")
            return self.read_row()
        return row

    def read_column(self):
        column = input("Introduce un numero (entre 1 y 8): ")
        if '1' <= column <= '8':
            column = ord(column) - ord('1')
        else:
            print("Introduzca un numero entre la 1 y 8")
            return self.read_column()
        return column

    def read_turn(self):
        row = self.read_row()
        column = self.read_column()
        return (row, column)


end = False

board = Board()
player = Player()

board.draw()

while not end:
    turn: (int,int) = player.read_turn()
    result = board.check(turn)
    if result == WATER:
        print("WATER!!!!")
    else:
        print("HIT!!!!")
    board.draw()
    end = board.check_end()

