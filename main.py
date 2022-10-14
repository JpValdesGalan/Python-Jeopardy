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

def change_board (board, inp_row, inp_column):
    board[inp_row][inp_column] = ' x '

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
    board_random = np.array(np.arange(0, 36))
    np.random.shuffle(board_random)
    print(board_random)

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
        
        # Convertimos nuestro index de matriz a lista
        input_idx = (int(input_row)*6) + (int(input_column))

        # Le damos el valor a la pregunta dependiendo de su posicion
        points = 600 - int(input_row)*100
        print(f'Playing for {points} points!!!\n')

        # Obtenemos el valor al que le pertenece al index en nuestro board random
        game_tile = board_random[input_idx]
        question = questions[game_tile]['Question']
        answer = str(questions[game_tile]['Answer'])

        # Imprimimos pantalla de pregunta
        print(f'ITS {team.name} TURN\n')
        print(question)
        result = input()
        os.system('cls')
        while result.isdigit() != True:
            print(f'ITS {team.name} TURN')
            print(question)
            result = input()
            os.system('cls')

        # Comparamos input del usuario con la respuesta
        if result == answer:
            print('RESPUESTA CORRECTA! :D')
            change_board(board, int(input_row), int(input_column))
            team.add_points(points)
        else:
            print('RESPUESTA INCORRECTA :(')

        exit_game = input('Press any key to Continue\tExit (0)')
        os.system('cls')

        if exit_game == 0:
            if team1.points > team2.points:
                print(f'The winner is {team1.name} with {team1.points} points!')
            elif team2.points > team1.points:
                print(f'The winner is {team2.name} with {team2.points} points!')
            else:
                print('Draw')
            game_flag = False
        

        # [game_tile]['Question'] == Pregunta
        # [game_tile]['Answer'] == Respuesta
        if team_flag == True: team_flag = False
        else: team_flag = True