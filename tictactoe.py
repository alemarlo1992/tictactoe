""" Tic Tac Toe game using OOP"""
import os 

class Board(object):
    """ Board for tic tac toe """
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        print(f"{self.cells[1]} | {self.cells[2]} | {self.cells[3]}")
        print("__________")
        print(f"{self.cells[4]} | {self.cells[5]} | {self.cells[6]}")
        print("__________")
        print(f"{self.cells[7]} | {self.cells[8]} | {self.cells[9]}")

    def update_cell(self, cell_num, player):
        """ Update cell after user input """
        self.cells[cell_num] = player 

board = Board()

def welcome_message():
    """ Welcome message for players """
    print("Hello! Welcome to Tic Tac Toe")

def refresh_screen():
    """ Refresh screen when there has been an update to board """ 

    # clear screen 
    os.system("clear")

    # print welcome message 
    welcome_message()

    #display board to player 
    board.display()

while True: 
    # start by refreshing terminal 
    refresh_screen()

    # Player X input 
    x = int(input("Player X: Choose cell 1 - 9 >"))

    board.update_cell(x, "X")

    refresh_screen()

    # Player O input
    o = int(input("Player O: Choose cell 1 - 9 >"))

    board.update_cell(o, "O")

    refresh_screen()




