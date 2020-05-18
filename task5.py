# Необходимо реализовать модуль divisor_master.

#Генерация случайного числа от 1 до 1000:
import random
sequence_num =list( range(1, 1001))
num_x=random.choice(sequence_num)

# 1) проверка случайного числа на простоту;
def prime_num(number):
   divisor = 2
   while number % divisor!= 0:
       divisor += 1
   return divisor == number

print("Случайное число",num_x, 'простое -', prime_num(num_x))

# 2) Определение список всех делителей случайного числа:
def spis_del(num_x):
    result = []
    i = 2
    while i * i <= num_x:
        if num_x % i == 0:
            num_x //= i
            result.append(i)
        else:
            i += 1
    if num_x > 1:
        result.append(num_x)
    return result
print('Делители числа - ', num_x, '-',spis_del(num_x))


# 3) Определение самого большого простого делителя числа
def divider(num_x):
    num = spis_del(num_x)
    max_num = 0
    for i in num:
        if i > max_num:
            max_num = i
    return (max_num)
print('Самый простой делитель числа -', num_x, '-', divider(num_x))