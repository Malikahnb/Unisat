# 1 task
#  Решите квадратное уравнение a*x**2+b*x+c=0.
import math

print("a*x**2+b*x+c=0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discriminant = b ** 2 - 4 * a * c
print("Discriminant = %.2f" % discriminant)

if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("x1 = %.2f \n x2 = %.2f" % (x1, x2))
elif discriminant == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("No roots")


# -------------------------------------------
# 2 task
name = 'Ad Astra'

for i in name:
    print(hex(ord(i)), end=' ')

# ---------------------------------------------
# 3 task
# Dля всех чисел A от 1 до 100 вывести 3*2-1, если A четное,  и A**2, если A нечетное
a = int(input('Number from 1 to 100: '))

if a in range(1, 101):
    if a % 2 == 0:
        print(3*2-1)
    else:
        print(a**2)

# ------------------------------------------------
# 4 task
# Сложите последовательность чисел, вводимых с клавиатуры. Признак окончания ввода — ввод числа 0. Напечатайте
# полученную сумму

num = 1
result = 0

while num != 0:
    num = int(input('Enter the number: '))
    if num != 0:
        result += num
    else:
        break

print(result)

# ---------------------------------------------------
# 5 task


def binary_year(year):
    if year >= 1:
        binary_year(year // 2)
    print(year % 2, end='')


binary_year(2004)

# -----------------------------------------------------
# 6 task


def hex_year(number):
    num = int(number, 2)
    hex_num = format(num, 'x')
    return (hex_num)


print(hex_year('011111010100'))
