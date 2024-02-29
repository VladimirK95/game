#Создание игрового поля
field = [1,2,3,
         4,5,6,
         7,8,9]

#Создание победных линий
wins = [[0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]]

#Вывод игрового поля на экран
def print_field():
    print(field[0], end = " ")
    print(field[1], end = " ")
    print(field[2])

    print(field[3], end = " ")
    print(field[4], end = " ")
    print(field[5])

    print(field[6], end = " ")
    print(field[7], end = " ")
    print(field[8])

#Сделать ход
def step_field(step,symbol):
    ind = field.index(step)
    field[ind] = symbol

#Проверить текущий результат
def get_result():
    win = ""

    for i in wins:
        if field[i[0]] == "X" and field[i[1]] == "X" and field[i[2]] == "X":
            win = "X"
        if field[i[0]] == "O" and field[i[1]] == "O" and field[i[2]] == "O":
            win = "O"
    return win
#Основной код
game_over = False
player = True

while game_over == False:

    #Показываю игровое поле
    print_field()

    #Спрашиваю игрока куда ходить
    if player == True:
        symbol = "X"
        step = int(input("Игрок 1, ходи: "))
    else:
        symbol = "O"
        step = int(input("Человек 2, ходи: "))

    #Делаем ход в указанную ячейку игрового поля
    step_field(step,symbol)

    #Выявляем победителя
    win = get_result()
    if win != "":
        game_over = True
    else:
        game_over = False

    player = not(player)

#Игра окончена, показываем игровое поле и объявляем кто победил
print_field()
print("Победил", win)