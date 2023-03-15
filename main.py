""" Не судите строго - на что ума хватило,то и написал.Это мой первый длинный код.
 100% Тут можно было сократить количество строк кода единиц на 100... используя
 другие методы и функция и условия с циклами. Игра работает, хоть и отображение игрового поля кривовато реализовано"""
# Создатель Павел Андреевич С. PDEV-27
import time
print('*' * 8, 'Приветствую в моей первой игре "Крестики - нолики" ! ', '*' * 8)
time.sleep(1)
print(' Выбирай за кого будешь играть ! ')
time.sleep(0.5)
while True:
    side = input(' Нажми "k" ,чтобы выбрать крестик или нажми "o" ,чтобы играть за нолик : ')
    if side == 'o':
        print(' Добро пожаловать в отряд нулей ')
        break
    elif side == 'k':
        print(' Ты выбрал темную сторону крестов ')
        break
    else:
        print(' Попробуй ввести еще раз : ')
print(' По правилам игры крестики ходят первыми ! ')
print(' Активное поле 3x3')
# создаю пустые списки, которые будут заполнятся крестиками и ноликами в процессе игры
a = ["", "", ""]
b = ["", "", ""]
c = ["", "", ""]


# move_krest - функция хода крестиков
def move_krest():
    while True:
        print(' ', 0, 1, 2, sep="   ")
        print(f'0 {a}', f'1 {b}', f'2 {c}', sep='\n')
        print('Ходят крестики!')
        coordinates = input('Введи координаты куда хочешь поставить крестик в формате 0-0 1-1 2-2 и т.п : ')
        if coordinates == '0-0':
            a[0] = 'X'
            break
        elif coordinates == '0-1':
            a[1] = 'X'
            break
        elif coordinates == '0-2':
            a[2] = 'X'
            break
        elif coordinates == '1-0':
            b[0] = 'X'
            break
        elif coordinates == '1-1':
            b[1] = 'X'
            break
        elif coordinates == '1-2':
            b[2] = 'X'
            break
        elif coordinates == '2-0':
            c[0] = 'X'
            break
        elif coordinates == '2-1':
            c[1] = 'X'
            break
        elif coordinates == '2-2':
            c[2] = 'X'
            break
        else:
            print('Неверный ввод! Попробуй снова!')


# move_zero - функция хода ноликов
def move_zero():
    while True:
        print(' ', 0, 1, 2, sep="   ")
        print(f'0 {a}', f'1 {b}', f'2 {c}', sep='\n')
        print('Ходят нолики!')
        coordinates = input('Введи координаты куда хочешь поставить нолик в формате 0-0 1-1 2-2 и т.п : ')
        if coordinates == '0-0':
            a[0] = 0
            break
        elif coordinates == '0-1':
            a[1] = 0
            break
        elif coordinates == '0-2':
            a[2] = 0
            break
        elif coordinates == '1-0':
            b[0] = 0
            break
        elif coordinates == '1-1':
            b[1] = 0
            break
        elif coordinates == '1-2':
            b[2] = 0
            break
        elif coordinates == '2-0':
            c[0] = 0
            break
        elif coordinates == '2-1':
            c[1] = 0
            break
        elif coordinates == '2-2':
            c[2] = 0
            break
        else:
            print('Неверный ввод! Попробуй снова!')


while True:
    move_krest()
    if (a[0] and (a[1] and a[2])) or (a[0] and (b[0] and c[0])) or (a[0] and (b[1] and c[2]))\
            or (a[1] and (b[1] and c[1])) or (a[2] and (b[2] and c[2])) or (b[0] and (b[1] and b[2]))\
            or (c[0] and (c[1] and c[2])) or (a[2] and (b[1] and c[0])) == 'X':
        print(' ', 0, 1, 2, sep="   ")
        print(f'0 {a}', f'1 {b}', f'2 {c}', sep='\n')
        print('Армия крестов победила!')
        print('*' * 8, 'Игра завершена!', '*' * 8)
        time.sleep(3)
        break
    move_zero()
    if (a[0] and (a[1] and a[2])) or (a[0] and (b[0] and c[0])) or (a[0] and (b[1] and c[2]))\
            or (a[1] and (b[1] and c[1])) or (a[2] and (b[2] and c[2])) or (b[0] and (b[1] and b[2]))\
            or (c[0] and (c[1] and c[2])) or (a[2] and (b[1] and c[0])) == 0:
        print(' ', 0, 1, 2, sep="   ")
        print(f'0 {a}', f'1 {b}', f'2 {c}', sep='\n')
        print('Нолики победили!')
        print('*' * 8, 'Игра завершена!', '*' * 8)
        time.sleep(3)
        break
