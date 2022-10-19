import random
import pandas as pd
import os

board =[['600', '600', '600', '600', '600', '600'],
        ['500', '500', '500', '500', '500', '500'],
        ['400', '400', '400', '400', '400', '400'],
        ['300', '300', '300', '300', '300', '300'],
        ['200', '200', '200', '200', '200', '200'],
        ['100', '100', '100', '100', '100', '100']]

def generate_random_board ():
    ''' Genera una lista con numeros del 1-36 acomodados de manera aleatoria para que el tablero sea diferente cada juego'''
    random_board = []
    for i in range(36):
        random_board.append(i)
    random.shuffle(random_board)
    return random_board

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
    
def init_teams():
    ''' Pedimos a los jugadores el nombre de cada equipo y retornamos su nombre y sus puntos en 0 de ambos equipos '''
    # Pedimos nombre de cada jugador/equipo
    os.system('cls')
    name = input('Introduce Team 1 name: ')
    team1_name = name
    name = input('Introduce Team 2 name: ')
    team2_name = name
    os.system('cls')
    # Inicializamos puntos de cada equipo
    team1_points = 0
    team2_points = 0
    return team1_name, team1_points, team2_name, team2_points
    
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

    input_idx = (int(input_row)*6) + (int(input_column))

    return input_row, input_column, input_idx

def question_screen():
    # Imprimimos pantalla de pregunta
    print(f'ITS {team_name} TURN\n')
    print(question,'\n')
    # Leemos resultado
    result = input('Answer: ')
    os.system('cls')
    while result.isdigit() != True:
        print(f'ITS {team_name} TURN')
        print(question)
        result = input()
        os.system('cls')
    return result

def change_board (board, inp_row, inp_column):
    ''' Cambia el valor que se muestra del tablero por una x '''
    board[inp_row][inp_column] = ' x '

def change_random_board(random_board, indx):
    ''' Cambia el valor que tiene la lista de random_board por null '''
    random_board[indx] = -1

def print_screen():
    print('Team:', team1_name)
    print('Points: ', team1_points)
    print('Team:', team2_name)
    print('Points: ', team2_points)
    print_board(board)
    print(f'ITS {team_name} TURN')
    
def exit_game():
    exit_input = input('Press ENTER to Continue\t\tExit (0)')
    os.system('cls')
    if exit_input == '0':
        if team1_points > team2_points:
            print(f'The winner is {team1_name}!\nWith {team1_points} points')
        elif team2_points > team1_points:
            print(f'The winner is {team2_name}!\nWith {team2_points} points')
        else:
            print('Draw')
        return False
    else:
        return True

if __name__ == '__main__':
    # jeopardy.csv contiene las preguntas del jeopardy
    # Cargamos el cv y convertimos a dictionario
    filename = 'jeopardy.xlsx'
    questions = pd.read_excel(filename).to_dict('index')
    
    # Inicializamos flags para el juego y equipos
    game_flag = True    # True sigue el juego
    team_flag = True    # True = Team1 | False = Team2

    # Generamos nuestro board con preguntas random
    random_board = generate_random_board()

    # Init Teams
    team1_name, team1_points, team2_name, team2_points = init_teams()

    # Inicia Juego
    while game_flag == True:

        # Asignamos el equipo de la ronda
        if team_flag == True: team_name = team1_name
        else: team_name = team2_name

        # Llama a funcion que lee el input y lo guarda en estas variables
        input_row, input_column, input_idx = read_input()

        # Con el indice que nos indico el usuario saber cual es la casilla que eligio
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

        # Pantalla de pregunta
        result = question_screen()

        # Comparamos input del usuario con la respuesta
        if result == answer:
            print('CORRECT ANSWER! :D')
            change_board(board, int(input_row), int(input_column))
            change_random_board(random_board, int(input_idx))
            if team_flag == True:
                team1_points += points
            else:
                team2_points += points
        else:
            print('INCORRECT ANSWER :(')
            
        # Cambiar de equipo ya que termino el turno
        if team_flag == True: team_flag = False
        else: team_flag = True

        # Salir del juego
        game_flag = exit_game()