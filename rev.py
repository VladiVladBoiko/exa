#Обратное число
#Ввод числа
a = int(input('Введите число: '))
reversed_number = 0
#Расчет
def rev(a):
    num_str = str(a)
    reversed_num_str = num_str[::-1]
    reversed_num = int(reversed_num_str)
    return reversed_num
    
print ( ( rev(a) ) )
