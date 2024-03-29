# 1. Даны значения величины заработной платы заемщиков банка (zp)
# и значения их поведенческого кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Используя математические операции, посчитать коэффициенты линейной регрессии,
# приняв за X заработную плату (то есть, zp - признак),
# а за y - значения скорингового балла (то есть, ks - целевая переменная).
# Произвести расчет как с использованием intercept, так и без.

import numpy as np

x = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
n = len(x)
print(n)
# 10

b_1 = (np.mean(x * y) - np.mean(x) * np.mean(y)) / (np.mean(x ** 2) - np.mean(x) ** 2)
print(b_1)
# 2.620538882402765

b_0 = np.mean(y) - b_1 * np.mean(x)
print(b_0)
# 444.1773573243596

# без интерсепта
x = x.reshape(10, 1)
print(x)

y = y.reshape(10, 1)
print(y)

b = np.dot(np.linalg.inv(np.dot(x.T, x)), x.T @ y)
print(b)
# 5.88982042

# с интерсептом
x = np.hstack([np.ones((10, 1)), x])
print(x)

b = np.dot(np.linalg.inv(np.dot(x.T, x)), x.T @ y)
print(b)

# [[444.17735732]
#  [  2.62053888]]


# 2. Посчитать коэффициент линейной регрессии при заработной плате (zp),
# используя градиентный спуск (без intercept).

# без интерсепта
x = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

def mse_(b_1, y=y, x=x, n=10):
    return np.sum((b_1 * x - y) ** 2) / n


b_1 = 0.1
alpha = 1e-6

for i in range(10000):
    b_1 -= alpha * (2 / n) * np.sum((b_1 * x - y) * x)
    if i % 5000 == 0:
        print('Итерация: {i}, b_1 = {b_1}, mse = {mse}'.format(i=i, b_1=b_1, mse=mse_(b_1)))

# Итерация: 0, b_1 = 0.25952808, mse = 493237.7212546963
# Итерация: 5000, b_1 = 5.889820420132673, mse = 56516.85841571943


# 3. В каких случаях для вычисления доверительных интервалов и
# проверки статистических гипотез используется таблица значений функции Лапласа,
# а в каких - таблица критических точек распределения Стьюдента?
# таблица значений функции Лапласа используется, когда известно среднеквадратическое отклонение
# таблица критических точек распределения Стьюдента используется, когда не известно среднеквадратическое отклонение

# *4. Произвести вычисления как в пункте 2, но с вычислением intercept.
# Учесть, что изменение коэффициентов должно производиться на каждом шаге
# одновременно (то есть изменение одного коэффициента
# не должно влиять на изменение другого во время одной итерации).
# с интерсептом
x = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

b_1 = 0.1
b_0 = 0.1
alpha = 5e-5


def mse_(b_0, b_1, y=y, x=x, n=10):
    return np.sum((b_0 + b_1 * x - y) ** 2) / n


for i in range(750000):
    y_hat = b_0 + b_1 * x
    b_0 -= alpha * (2 / n) * np.sum((y_hat - y))
    b_1 -= alpha * (2 / n) * np.sum((y_hat - y) * x)
    if i % 30000 == 0:
        print('Итерация: {i}, b_0 = {b_0}, b_1 = {b_1}, mse = {mse}'.format(i=i, b_0=b_0, b_1=b_1, mse=mse_(b_0, b_1)))
# Итерация: 690000, b_0 = 444.1773461989089, b_1 = 2.620538964291002, mse = 6470.414201176691
# Итерация: 720000, b_0 = 444.17735212636813, b_1 = 2.620538920662281, mse = 6470.414201176669