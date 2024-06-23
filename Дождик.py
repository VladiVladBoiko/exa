from random import randint
import time
#Ввод имен играющих
player1 = input('Введите имя 1-го игрока ')
player2 = input('Введите имя 2-го игрока ')
#Моделирование бросания кубика первым играющим
print('Кубик бросает', player1)
time.sleep(2)
n1 = randint(1, 6)
print('Выпало:', n1)
#Моделирование бросания кубика вторым играющим
print('Кубик бросает', player2)
time.sleep(2)
n2 = randint(1, 6)
print('Выпало:', n2)
