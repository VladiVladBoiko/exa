# процент на заказы
a = int(input ( "Количество заказов на маршруте: "))
b = int(input ( "Количество выполненых заказов: "))
e = int(input ( 'Сумма продаж: ' ))
o = 100
goods1 = int(input ( 'Товаров загружено штук: '))
goods2 = int(input( 'Товаров продано штук: '))
if e <= 120000:
    g1 = 0
f = goods2 * o / goods1
# коэффицент суммма
if e < 80000:
    c = (e * 0.0326)
if e >= 80000:
 c = (e * 0.0332)
if e >= 90000:
 c = (e * 0.0338)
if e >= 100000: 
 c = (e * 0.0345)
if e >= 110000:
 g1 = (e - 90000)
 x1 = (0.06)
 h3 = g1/10000
 g2 = 3.45 + x1 * round( h3)
 c4 = g2 / 100
 c = e * c4
print ('оплата от суммы продаж: ' + str(round( c )))
# коэффицент заказы
d = b * o / a
if d < 75:
 w = 0
if d >= 75:
    w = d - 65
g = c * w / o
print ("доплата за выкупаемость заказов: " + str(round( g )))
# коэффицент товаров
if f < 32:
 m = 0
if f >= 32:
       f <= 42
       f1 = (f - 32)
       f2 = (f - 27 + f1 * 2 )
       y1 = (f2 / 100)
       m = (c * y1)
if f > 42:
    m = (c * 0.35)
    print ("доплата за выкупаемость товаров: " + str(round( m )))                            
# итог
pas = c + g + m
print ('итог дня: ' + str(round (pas)) )
testfile = open('numbers.txt', 'a')
testfile.write ( str(round( pas)) + '\n')
testfile.close( )
input ( )
