#Ввод числа
a = int( input( "Введите число: "))
#Функции
def positive():
    return ("Число " + str(a) +" положительное" )
def negative():
    return ("Число " + str(a) +" отрицательное" )
def test():
    if a>=0:
        return positive()
    else:
        return negative()
#Вывод результата
print( test() )


