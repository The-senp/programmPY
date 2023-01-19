import math

r = float(input('Введите радиус окружности: '))
n = int(input('Введите колличество углов: '))
p = 2*r*n*math.sin(math.pi/n)*math.cos(math.pi/n)

print(f'Периметр {n}-угольника, описанного около окружности радиуса {r} равен {p}')
