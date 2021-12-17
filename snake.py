from pynput.keyboard import Key, Events
import random
import os


###########################
######## Fonctions ########
###########################


def movement(direction):
    global matrix, snake
    reset_matrix()
    transition = []
    for i in snake[0]:
        transition.append(i)
    if direction == 'left':
        transition[1] -= 1
    elif direction == 'right':
        transition[1] += 1
    elif direction == 'up':
        transition[0] -= 1
    else: transition[0] += 1
    snake.insert(0, transition)
    last = len(snake)
    snake.pop(last - 1)
    for coordinates in snake[1:]:
        matrix[coordinates[0]][coordinates[1]] = 'o'
    for coordinates in snake[:1]:
        matrix[coordinates[0]][coordinates[1]] = 'O'
    print_matrix()
    apple()
    print('Your score :', len(snake) - 2)


def apple():
    global x_apple, y_apple, rotten_apple
    head = []
    back = []
    for i in snake[0]:
        head.append(i)
    if head[0] == y_apple and head[1] == x_apple:
        for j in snake[-1]:
            back.append(j)
        snake.append(back)
        rotten_apple = 0
        test_apple()
    else: rotten_apple += 1
    if rotten_apple == 10:
        rotten_apple = 0
        rotten_apple_function()


def test_apple():
    global snake, x_apple, y_apple, obstacles
    while True:
        x_apple = random.randint(1, 9)
        y_apple = random.randint(1, 9)
        test = []
        test.append(y_apple)
        test.append(x_apple)
        if test in snake:
            continue
        if test in obstacles:
            continue
        else: break


def rotten_apple_function():
    global obstacles, y_apple, x_apple
    obstacles.append([y_apple, x_apple])
    test_apple()


def game_over():
    global obstacles
    head = []
    for i in snake[0]:
        head.append(i)
    if head[0] in [0, 10] or head[1] in [0, 10]:
        print('Game Over')
        return False
    for j in snake[1:]:
        if head == j:
            print('Game Over')
            return False
    for coordinates in obstacles:
        if head == coordinates:
            print('Game Over')
            return False
    return True


def clear():
    if os.name == 'posix':
        os.system('clear')
    else: os.system('cls')


def print_matrix():
    clear()
    for ligne in matrix:
        for i in ligne:
            print(i, ' ', end='')
        print('\t')


def reset_matrix():
    global matrix, obstacles
    matrix =  [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
               ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
               ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
               ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
               ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
               ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
               ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
               ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
               ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
               ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
               ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
               ]
    if rotten_apple < 9:
        matrix[y_apple][x_apple] = 8 - rotten_apple
    else:
        matrix[y_apple][x_apple] = '='
    for coordinates in obstacles:
        matrix[coordinates[0]][coordinates[1]] = '='


###########################
########## CODE ###########
###########################


matrix =   [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', ' ', ' ', 'o', 'O', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
           ]


snake = [[5, 5], [5, 4]]


obstacles = []
rotten_apple = 0


test_apple()


matrix[y_apple][x_apple] = '9'


print_matrix()


iterator = 0


direction = ''
with Events() as events:
    while game_over() is True:
        event = events.get(1)
        if (event is None) and (iterator == 0):
            direction = 'right'
            movement(direction)
        elif (event is None) and (iterator > 0):
            movement(direction)
        else:
            if 'Press' in str(format(event)):
                continue
            if (event.key == Key.left) and (direction != 'right'):
                iterator += 1
                direction = 'left'
                movement(direction)
            elif (event.key == Key.right) and (direction != 'left'):
                iterator += 1
                direction = 'right'
                movement(direction)
            elif (event.key == Key.up) and (direction != 'down'):
                iterator += 1
                direction = 'up'
                movement(direction)
            elif (event.key == Key.down) and (direction != 'up'):
                iterator += 1
                direction = 'down'
                movement(direction)
