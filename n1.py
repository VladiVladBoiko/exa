#Запрос числа и действия с числом
#Ввод данных
n = int(input('Введите число: '))
b = int(input('Что нужно сделать? (1- вывести сумму цифр числа, 2- максимальную цифру числа, 3- минимальную цифру числа) - '))
#Функции

def summa_n():
    return int(n*(n+1)/2)

def ma(n):
    n = n//10
    m = n%10
    while n > 0:
        if n % 10 > m:
            m = n % 10
        n = n//10
    return (m)

def mi(n):
    n = n//10
    m = n%10
    while n > 0:
        if n % 10 < m:
            m = n % 10
        n = n//10
    return (m)
def func():
    if b == 1:
        return summa_n()
    elif b == 2:
        return ma(n)
    elif b == 3:
        return mi(n)
    else:
        return "Нужно выбрать из доступных вариантов"

print ( func() )