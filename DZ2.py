# Интерфейс 6 на 6 с полями от 1 до 6, с  пустотой в уголке СДЕЛАНО?
# Класс доски с размещенными кораблями
# Сделать класс с кораблей с инфой о его положение на карте
# Комп ходит рандомно, но не стреляет туда где он уже стрелял
# корабли не могут соприкасаться
# корабли один трешник, два двушника и четыре единички
# Запрет на выстрел в туже точку, при ошибки исключение
# X подбитые T промохи
# при возниконовение чего делать что то?
# победитель убивший всех

# сделать класс. в котором будет статус поля. и игроку и компьютеру исользуя этот класс присвоить разные поля, и по вызову этой функции выводить поле
import random
import statistics


def pole(s):
    print(" ", 1, 2, 3, 4, 5, 6)
    for i in range(1, 7):
        print(i, end=" ")
        for j in range(1, 7):
            print(s[i][j], end=" ")
        print()


class Desk:

    def status(self, s):
        return s

    def start_location_one(self, pole, x, y):
        self.x = x
        self.y = y
        self.pole = pole
        # ОДИН ЗДОРОВЫЙ КОСТЫЛЬ
        if pole[x][y] == "O":
            if x == 1 and y == 1:
                if pole[x][y + 1] == pole[x][y] == pole[x + 1][y] == pole[x + 1][y + 1] == "O":
                    pole[x][y] = "S"
            if x == 6 and y == 6:
                if pole[x][y - 1] == pole[x][y] == pole[x - 1][y] == pole[x - 1][y - 1] == "O":
                    pole[x][y] = "S"
            if x == 1 and y == 6:
                if pole[x][y - 1] == pole[x][y] == pole[x + 1][y] == pole[x + 1][y - 1] == "O":
                    pole[x][y] = "S"
            if x == 6 and y == 1:
                if pole[x][y + 1] == pole[x][y] == pole[x - 1][y] == pole[x - 1][y + 1] == "O":
                    pole[x][y] = "S"
            if x == 1 and 1 < y < 6:
                if pole[x][y + 1] == pole[x][y] == pole[x][y - 1] == pole[x + 1][y + 1] == pole[x + 1][y] == pole[x + 1][y - 1] == "O":
                    pole[x][y] = "S"
            if 1 < x < 6 and y == 1:
                if pole[x - 1][y] == pole[x][y] == pole[x + 1][y] == pole[x - 1][y + 1] == pole[x][y + 1] == pole[x + 1][y + 1] == "O":
                    pole[x][y] = "S"
            if x == 6 and 1 < y < 6:
                if pole[x][y + 1] == pole[x][y] == pole[x][y - 1] == pole[x - 1][y + 1] == pole[x - 1][y] == pole[x - 1][y - 1] == "O":
                    pole[x][y] = "S"
            if 1 < x < 6 and y == 6:
                if pole[x - 1][y] == pole[x][y] == pole[x + 1][y] == pole[x - 1][y - 1] == pole[x][y - 1] == pole[x + 1][y - 1] == "O":
                    pole[x][y] = "S"
            if 1 < x < 6 and 1 < y < 6:
                if pole[x][y - 1] == pole[x][y] == pole[x][y + 1] == pole[x + 1][y - 1] == pole[x + 1][y] == pole[x + 1][y + 1] == pole[x - 1][y - 1] == pole[x - 1][y] == pole[x - 1][y + 1] == "O":
                    pole[x][y] = "S"  # Как тут расписать по другому, но с той же логикой ибо он уходит за список и возникает ошибка

    def start_location_two(self, pole, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        self.pole = pole

        if pole[x1][y1] == pole[x2][y2] == "O":
            if x1 == x2:  # gorizontal
                if x1 == 1 and y1 == 1:
                    if pole[x1][y1 + 2] == pole[x1 + 1][y1] == pole[x1 + 1][y1 + 1] == pole[x1 + 1][y1 + 2] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"

                if x1 == 6 and y2 == 6:
                    if pole[x1][y1 - 1] == pole[x1 - 1][y1 - 1] == pole[x1 - 1][y1] == pole[x1 - 1][y1 + 1] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"

                if x1 == 1 and y2 == 6:
                    if pole[x1][y1 - 1] == pole[x1 + 1][y1 - 1] == pole[x1 + 1][y1] == pole[x1 + 1][y1 + 1] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"

                if x1 == 6 and y1 == 1:
                    if pole[x1][y1 + 2] == pole[x1 - 1][y1] == pole[x1 - 1][y1 + 1] == pole[x1 - 1][y1 + 2] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"

                if x1 == 1 and 1 < y1 < 6 and 1 < y2 < 6:
                    if pole[x1][y1 - 1] == pole[x1][y1 + 2] == pole[x1 + 1][y1 - 1] == pole[x1 + 1][y1] == pole[x1 + 1][y1 + 1] == pole[x1 + 1][y1 + 2] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"

                if 1 < x1 < 6 and y1 == 1:
                    if pole[x1 - 1][y1] == pole[x1 - 1][y1 + 1] == pole[x1 - 1][y1 + 2] == pole[x1][y1 + 2] == pole[x1 + 1][y1 + 2] == pole[x1 + 1][y1 + 1] == pole[x1 + 1][y1] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"

                if x1 == 6 and 1 < y1 < 6 and 1 < y2 < 6:
                    if pole[x1][y1 - 1] == pole[x1 - 1][y1 - 1] == pole[x1 - 1][y1] == pole[x1 - 1][y1 + 1] == pole[x1 - 1][y1 + 2] == pole[x1][y1 + 2] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"

                if 1 < x1 < 6 and y2 == 6:
                    if pole[x1 - 1][y1 - 1] == pole[x1 - 1][y1] == pole[x1 - 1][y1 + 1] == pole[x1][y1 - 1] == pole[x1 + 1][y1 - 1] == pole[x1 + 1][y1] == pole[x1 + 1][y1 + 1] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"

                if 1 < x1 < 6 and 1 < y1 < 6 and 1 < y2 < 6:
                    if pole[x1 - 1][y1 - 1] == pole[x1 - 1][y1] == pole[x1 - 1][y1 + 1] == pole[x1 - 1][y1 + 2] == pole[x1 + 1][y1 - 1] == pole[x1 + 1][y1] == pole[x1 + 1][y1 + 1] == pole[x1 + 1][y1 + 2] == pole[x1][y1 + 2] == pole[x1][y1 - 1] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"

            if y1 == y2:  # vertical
                if x1 == 1 and y1 == 1:
                    if pole[x1][y1 + 1] == pole[x1 + 1][y1 + 1] == pole[x1 + 2][y1 + 1] == pole[x1 + 2][y1] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"

                if x2 == 6 and y1 == 6:
                    if pole[x1 - 1][y1] == pole[x1 - 1][y1 - 1] == pole[x1][y1 - 1] == pole[x1 + 1][y1 - 1] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"

                if x1 == 1 and y1 == 6:
                    if pole[x1][y1 - 1] == pole[x1 + 1][y1 - 1] == pole[x1 + 2][y1 - 1] == pole[x1 + 2][y1] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"

                if x2 == 6 and y1 == 1:
                    if pole[x1 - 1][y1] == pole[x1 - 1][y1 + 1] == pole[x1][y1 + 1] == pole[x1 + 1][y1 + 1] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"

                if x1 == 1 and 1 < y1 < 6:
                    if pole[x1][y1 - 1] == pole[x1][y1 + 1] == pole[x1 + 1][y1 - 1] == pole[x1 + 1][y1 + 1] == pole[x1 + 2][y1 - 1] == pole[x1 + 2][y1] == pole[x1 + 2][y1 + 1] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"

                if 1 < x1 < 6 and 1 < x2 < 6 and y1 == 1:
                    if pole[x1 - 1][y1] == pole[x1 - 1][y1 + 1] == pole[x1][y1 + 1] == pole[x1 + 1][y1 + 1] == pole[x1 + 2][y1 + 1] == pole[x1 + 2][y1] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"

                if x2 == 6 and 1 < y1 < 6:
                    if pole[x1 - 1][y1 - 1] == pole[x1 - 1][y1] == pole[x1 - 1][y1 + 1] == pole[x1][y1 - 1] == pole[x1][y1 + 1] == pole[x1 + 1][y1 - 1] == pole[x1 + 1][y1 + 1] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"

                if 1 < x1 < 6 and 1 < x2 < 6 and y2 == 6:
                    if pole[x1 - 1][y1 - 1] == pole[x1 - 1][y1] == pole[x1][y1 - 1] == pole[x1 + 1][y1 - 1] == pole[x1 + 2][y1 - 1] == pole[x1 + 2][y1] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"

                if 1 < x1 < 6 and 1 < x2 < 6 and 1 < y1 < 6:
                    if pole[x1 - 1][y1 - 1] == pole[x1 - 1][y1] == pole[x1 - 1][y1 + 1] == pole[x1][y1 - 1] == pole[x1][y1 + 1] == pole[x1 + 1][y1 - 1] == pole[x1 + 1][y1 + 1] == pole[x1 + 2][y1 - 1] == pole[x1 + 2][y1] == pole[x1 + 2][y1 + 1] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"

    def start_location_three(self, pole, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        k = [x1, x2, x3]
        p = [y1, y2, y3]
        x1, x2, x3 = min(x1, x2, x3), statistics.mean(k), max(x1, x2, x3)
        y1, y2, y3 = min(y1, y2, y3), statistics.mean(p), max(y1, y2, y3)
        self.pole = pole

        if pole[x1][y1] == pole[x2][y2] == pole[x3][y3] == "O":
            if x1 == x2 == x3:  # gorizontal
                if x1 == 1 and y1 == 1:
                    if pole[x1][y1 + 3] == pole[x1 + 1][y1] == pole[x1 + 1][y1 + 1] == pole[x1 + 1][y1 + 2] == pole[x1 + 1][y1 + 3] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"
                        pole[x3][y3] = "S"

                if x1 == 6 and y3 == 6:
                    if pole[x1][y1 - 1] == pole[x1 - 1][y1 - 1] == pole[x1 - 1][y1] == pole[x1 - 1][y1 + 1] == pole[x1 - 1][y1 + 2] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"
                        pole[x3][y3] = "S"

                if x1 == 1 and y3 == 6:
                    if pole[x1][y1 - 1] == pole[x1 + 1][y1 - 1] == pole[x1 + 1][y1] == pole[x1 + 1][y1 + 1] == pole[x1 - 1][y1 + 2] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"
                        pole[x3][y3] = "S"

                if x1 == 6 and y1 == 1:
                    if pole[x1][y1 + 3] == pole[x1 - 1][y1] == pole[x1 - 1][y1 + 1] == pole[x1 - 1][y1 + 2] == pole[x1 - 1][y1 + 3] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"
                        pole[x3][y3] = "S"

                if x1 == 1 and 1 < y1 < 6 and 1 < y2 < 6 and 1 < y3 < 6:
                    if pole[x1][y1 - 1] == pole[x1][y1 + 3] == pole[x1 + 1][y1 - 1] == pole[x1 + 1][y1] == pole[x1 + 1][y1 + 1] == pole[x1 + 1][y1 + 2] == pole[x1 + 1][y1 + 3] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"
                        pole[x3][y3] = "S"

                if 1 < x1 < 6 and y1 == 1:
                    if pole[x1 - 1][y1] == pole[x1 - 1][y1 + 1] == pole[x1 - 1][y1 + 2] == pole[x1 - 1][y1 + 3] == pole[x1][y1 + 3] == pole[x1 + 1][y1 + 2] == pole[x1 + 1][y1 + 1] == pole[x1 + 1][y1] == pole[x1 + 1][y1 + 3] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"
                        pole[x3][y3] = "S"

                if x1 == 6 and 1 < y1 < 6 and 1 < y2 < 6 and 1 < y3 < 6:
                    if pole[x1][y1 - 1] == pole[x1 - 1][y1 - 1] == pole[x1 - 1][y1] == pole[x1 - 1][y1 + 1] == pole[x1 - 1][y1 + 2] == pole[x1 - 1][y1 + 3] == pole[x1][y1 + 3] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"
                        pole[x3][y3] = "S"

                if 1 < x1 < 6 and y3 == 6:
                    if pole[x1 - 1][y1 - 1] == pole[x1 - 1][y1] == pole[x1 - 1][y1 + 1] == pole[x1][y1 - 1] == pole[x1 + 1][y1 - 1] == pole[x1 + 1][y1] == pole[x1 + 1][y1 + 1] == pole[x1 - 1][y1 + 3] == pole[x1 + 1][y1 + 3] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"
                        pole[x3][y3] = "S"

                if 1 < x1 < 6 and 1 < y1 < 6 and 1 < y2 < 6 and 1 < y3 < 6:
                    if pole[x1 - 1][y1 - 1] == pole[x1 - 1][y1] == pole[x1 - 1][y1 + 1] == pole[x1 - 1][y1 + 2] == pole[x1 + 1][y1 - 1] == pole[x1 + 1][y1] == pole[x1 + 1][y1 + 1] == pole[x1 + 1][y1 + 2] == pole[x1][y1 + 3] == pole[x1][y1 - 1] == pole[x1 - 1][y1 + 3] == pole[x1 + 1][y1 + 3] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"
                        pole[x3][y3] = "S"

            if y1 == y2 == y3:  # vertical
                if x1 == 1 and y1 == 1:
                    if pole[x1][y1 + 1] == pole[x1 + 1][y1 + 1] == pole[x1 + 2][y1 + 1] == pole[x1 + 3][y1 + 1] == pole[x + 3][y1] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"
                        pole[x3][y3] = "S"

                if x3 == 6 and y1 == 6:
                    if pole[x1 - 1][y1] == pole[x1 - 1][y1 - 1] == pole[x1][y1 - 1] == pole[x1 + 1][y1 - 1] == pole[x1 + 2][y1 - 1] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"
                        pole[x3][y3] = "S"

                if x1 == 1 and y1 == 6:
                    if pole[x1 + 3][y1] == pole[x1][y1 - 1] == pole[x1 + 1][y1 - 1] == pole[x1 + 2][y1 - 1] == pole[x1 + 3][y1 - 1] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"
                        pole[x3][y3] = "S"

                if x3 == 6 and y1 == 1:
                    if pole[x1 - 1][y1] == pole[x1 - 1][y1 + 1] == pole[x1][y1 + 1] == pole[x1 + 1][y1 + 1] == pole[x1 + 2][y1 + 1] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"
                        pole[x3][y3] = "S"

                if x1 == 1 and 1 < y1 < 6:
                    if pole[x1][y1 - 1] == pole[x1][y1 + 1] == pole[x1 + 1][y1 - 1] == pole[x1 + 1][y1 + 1] == pole[x1 + 2][y1 - 1] == pole[x1 + 2][y1 - 1] == pole[x1 + 3][y1 - 1] == pole[x1 + 3][y3] == pole[x1 + 3][y3 + 1] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"
                        pole[x3][y3] = "S"

                if 1 < x1 < 6 and 1 < x2 < 6 and 1 < x3 < 6 and y1 == 1:
                    if pole[x1 - 1][y1] == pole[x1 + 3][y1] == pole[x1 - 1][y1 + 1] == pole[x1][y1 + 1] == pole[x1 + 1][y1 + 1] == pole[x1 + 2][y1 + 1] == pole[x1 + 3][y1 + 1] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"
                        pole[x3][y3] = "S"

                if x3 == 6 and 1 < y1 < 6:
                    if pole[x1 - 1][y1 - 1] == pole[x1 - 1][y1] == pole[x1 - 1][y1 + 1] == pole[x1][y1 - 1] == pole[x1][y1 + 1] == pole[x1 + 1][y1 - 1] == pole[x1 + 1][y1 + 1] == pole[x1 + 2][y1 - 1] == pole[x1 + 2][y1 + 1] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"
                        pole[x3][y3] = "S"

                if 1 < x1 < 6 and 1 < x2 < 6 and 1 < x3 < 6 and y1 == 6:
                    if pole[x1 - 1][y1] == pole[x1 + 3][y1] == pole[x1 - 1][y1 - 1] == pole[x1][y1 - 1] == pole[x1 + 1][y1 - 1] == pole[x1 + 2][y1 - 1] == pole[x1 + 3][y1 - 1] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"
                        pole[x3][y3] = "S"

                if 1 < x1 < 6 and 1 < x2 < 6 and 1 < x3 < 6 and 1 < y1 < 6:
                    if pole[x1 - 1][y1 - 1] == pole[x1 - 1][y1] == pole[x1 - 1][y1 + 1] == pole[x1][y1 - 1] == pole[x1][y1 + 1] == pole[x1 + 1][y1 - 1] == pole[x1 + 1][y1 + 1] == pole[x1 + 2][y1 - 1] == pole[x1 + 2][y1 + 1] == pole[x1 + 3][y1 - 1] == pole[x1 + 3][y1] == pole[x1 + 3][y1 + 1] == "O":
                        pole[x1][y1] = "S"
                        pole[x2][y2] = "S"
                        pole[x3][y3] = "S"

    def gun_location_one(self, pole, x, y):
        self.x = x
        self.y = y
        self.pole = pole
        pole[x][y] = "S"


class Ships:
    pass  # 4 раза пройтись по единичке и вставить это в плейр доску и так же пройтись еще по двойкам и тройке


desk_enemy = [["O" for j in range(7)] for i in range(7)]
desk_player = [["O" for j in range(7)] for i in range(7)]
player = Desk()
enemy = Desk()
one = []
two = []
three = []

"""print("укажите где хотите поставить Единички, помните корабли не могут соприкасаться с друг другом")
for i in range(4):
    x, y = map(int, input().split())
    player.start_location_one(desk_player, x, y)
    one.append([x, y])
print("укажите где хотите поставить двойки, помните корабли не могут соприкасаться с друг другом")
for i in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    player.start_location_two(desk_player, x1, y1, x2, y2)
    two.append([x1, y1])
    two.append([x2, y2])
print("укажите где хотите поставить тройку, помните корабли не могут соприкасаться с друг другом")
for i in range(1):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    player.start_location_three(desk_player, x1, y1, x2, y2, x3, y3)
    three.append([x1, y1])
    three.append([x2, y2])
    three.append([x3, y3])"""
i = 1
desk_player[1][1] = "S"
desk_player[1][3] = "S"
desk_player[1][5] = "S"
desk_player[3][1] = "S"

desk_player[3][3] = "S"
desk_player[3][4] = "S"
desk_player[6][6] = "S"
desk_player[5][6] = "S"

desk_player[5][1] = "S"
desk_player[5][2] = "S"
desk_player[5][3] = "S"

desk_enemy[1][2] = "S"
desk_enemy[1][4] = "S"
desk_enemy[1][6] = "S"
desk_enemy[3][5] = "S"

desk_enemy[3][3] = "S"
desk_enemy[4][3] = "S"
desk_enemy[6][5] = "S"
desk_enemy[6][6] = "S"

desk_enemy[6][1] = "S"
desk_enemy[6][2] = "S"
desk_enemy[6][3] = "S"
count_player=0
count_enemy=0
q = 0
while i != 0:

    x, y = map(int, input("Куда стреляем?").split())
    if desk_enemy[x][y] == "S":
        print("Вы попали")
        desk_enemy[x][y] = "X"
        count_player+=1
        if x < 6 and y < 6 and desk_enemy[x][y - 1] != "S" and desk_enemy[x][y + 1] != "S" and desk_enemy[x - 1][y] != "S" and desk_enemy[x + 1][y] != "S":
            print("И потопили")
        elif x == 6 and desk_enemy[x][y - 1] != "S" and desk_enemy[x][y + 1] != "S" and desk_enemy[x - 1][y] != "S":
            print("И потопили")
        elif y == 6 and desk_enemy[x][y - 1] != "S" and desk_enemy[x - 1][y] != "S" and desk_enemy[x + 1][y] != "S":
            print("И потопили")

    else:
        print("Промох")
        desk_enemy[x][y] = "T"

    print("противник стрельнул сюда")
    while i != 0:
        z = random.randint(1, 6)
        c = random.randint(1, 6)
        if desk_player[z][c] == "S" or desk_player[z][c] == "O":
            if desk_player[z][c] == "S":
                desk_player[z][c] = "X"
                count_enemy+=1
                break
            else:
                desk_player[z][c] = "T"
                break
    if count_player==11 or count_enemy==11:
        break
pole(desk_player)
pole(desk_enemy)
