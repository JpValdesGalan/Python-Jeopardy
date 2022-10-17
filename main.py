import numpy as np
import pandas as pd
import os

board = [['600', '600', '600', '600', '600', '600'],
        ['500', '500', '500', '500', '500', '500'],
        ['400', '400', '400', '400', '400', '400'],
        ['300', '300', '300', '300', '300', '300'],
        ['200', '200', '200', '200', '200', '200'],
        ['100', '100', '100', '100', '100', '100']]
    
def print_board (board):
    ''' Imprime el tablero del juego '''
    count = 0
    print('\n  | ', end='')
    for i in range(len(board)):
        print(f' {i} ', end=' | ')
        if (i+1 == len(board)):
            print()
    for row in board:
        print(count, end=' | ')
        for val in row:
            print(val, end=' | ')
        count += 1
        print()
    print()

def read_input():
    ''' Lee el input que el usuario introduce '''
    # Preguntamos por input de linea
    print_screen()
    input_row = input('Introduce Row (0-5): ')
    os.system('cls')
    while (input_row.isdigit() != True or int(input_row) < 0 or int(input_row) > 5):
        print_screen()
        input_row = input('Introduce Row (0-5): ')
        os.system('cls')

    # Preguntamos por input de columna
    print_screen()
    input_column = input('Introduce Column (0-5): ')
    os.system('cls')
    while (input_column.isdigit() != True or int(input_column) < 0 or int(input_column) > 5):
        print_screen()
        input_column = input('Introduce Column (0-5): ')
        os.system('cls')

    if input_column == 0:
        input_idx = (int(input_row)*6) + (int(input_column))
    else:
        input_idx = (int(input_row)*6) + (int(input_column)+1)

    return input_row, input_column, input_idx


def change_board (board, inp_row, inp_column):
    ''' Cambia el valor que se muestra del tablero por una x '''
    board[inp_row][inp_column] = ' x '

def change_random_board(random_board, indx):
    ''' Cambia el valor que tiene la lista de random_board por null '''
    random_board[indx] = -1

class Team:
    def __init__ (self, name='', points=0):
        ''' Constructor de Team '''
        self.name = name
        self.points = points
    
    def __str__ (self):
        ''' Regresa string de Team '''
        return f'{self.name}\nPoints: {self.points}'

    def add_points (self, points):
        self.points += points

def print_screen():
    print(team1)
    print(team2)
    print_board(board)
    print(f'ITS {team.name} TURN')

if __name__ == '__main__':
    # jeopardy.csv contiene las preguntas del jeopardy
    # Cargamos el cv y convertimos a dictionario
    filename = 'jeopardy.csv'
    questions = pd.read_csv(filename, ).to_dict('index')
    
    game_flag = True    # True sigue el juego
    team_flag = True    # True = Team1 | False = Team2

    # Generamos nuestro board con preguntas random
    random_board = np.array(np.arange(0, 36))
    np.random.shuffle(random_board)
    print(random_board)

    # Pedimos nombre de cada jugador/equipo
    name = input('Introduce Team 1 name: ')
    team1 = Team(name, 0)
    os.system('cls')
    name = input('Introduce Team 2 name: ')
    team2 = Team(name, 0)
    os.system('cls')

    # Inicia Juego
    while game_flag == True:

        # Asignamos el equipo de la ronda
        if team_flag == True:
            team = team1
        else:
            team = team2

        # Llama a funcion que lee el input y lo guarda en estas variables
        input_row, input_column, input_idx = read_input()

        # Convertimos nuestro index de matriz a lista
        game_tile = random_board[input_idx]

        # Verificamos que no sea en una celda en la que ya se gano
        while game_tile == -1:
            print(f'This gametile has already been answered\nPlease choose another')
            input_row, input_column, input_idx = read_input()

        # Le damos el valor a la pregunta dependiendo de su posicion
        points = 600 - int(input_row)*100
        print(f'Playing for {points} points!!!\n')

        # Asignamos las preguntas y su correspondiente respuesta de la casilla
        question = questions[game_tile]['Question']
        answer = str(questions[game_tile]['Answer'])

        # Imprimimos pantalla de pregunta
        print(f'ITS {team.name} TURN\n')
        print(question)

        # Leemos resultado
        result = input()
        os.system('cls')
        while result.isdigit() != True:
            print(f'ITS {team.name} TURN')
            print(question)
            result = input()
            os.system('cls')

        # Comparamos input del usuario con la respuesta
        if result == answer:
            print('CORRECT ANSWER! :D')
            change_board(board, int(input_row), int(input_column))
            change_random_board(random_board, int(input_idx))
            team.add_points(points)
        else:
            print('INCORRECT ANSWER :(')

        exit_game = input('Press ENTER to Continue\tExit (0)')
        os.system('cls')

        # Salir del juego
        if exit_game == '0':
            if team1.points > team2.points:
                print(f'The winner is {team1.name}!\nWith {team1.points} points')
            elif team2.points > team1.points:
                print(f'The winner is {team2.name}!\nWith {team2.points} points')
            else:
                print('Draw')
            game_flag = False
        
        # [game_tile]['Question'] == Pregunta
        # [game_tile]['Answer'] == Respuesta
        if team_flag == True: team_flag = False
        else: team_flag = True