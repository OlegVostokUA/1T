import time

# for i in 1, 2, 3, 4, 5: # TITLE OF CYCLE
#     # print(i) # BODY OF CYCLE
#     print(i, end='')
#     print(i ** 3)


# word = 'alligator'
#
# for i in word: # TITLE OF CYCLE
#     # print(i) # BODY OF CYCLE
#     time.sleep(1)
#     print(i, end='')

# word = 'alligator'
#
# for number, i in enumerate(word): # TITLE OF CYCLE
#     # print(i) # BODY OF CYCLE
#     print(number+1, i)

# 1 to 100
# range (start, stop, step)
# var = range(1, 101, 1)
#
# for i in var:
#     print(i)

# for i in range(1, 101, 1):
#     print(i)
#
# for i in range(101):
#     print(i)


# running man
### 1 CASE
# health = 5
# weather = 'sun'
#
# for i in range(1, health+1):
#     time.sleep(1)
#     print('run 0.25l')
#     time.sleep(1)
#     print('run 0.50l')
#     time.sleep(1)
#     print('run 0.75l')
#     time.sleep(1)
#     print('run', i, 'lap')


# ### 2 CASE
# health = 5
# weather = 'sun'
#
# for i in range(1, health+1):
#     if weather == 'sun':
#         # print('run 0.25l')
#         # print('run 0.50l')
#         # print('run 0.75l')
#         print('run', i, 'lap')


# ### 3 CASE
# health = 5
# laps = 0
# weather = 'sun'
#
# for i in range(1, health + 1):
#     if weather == 'sun':
#         # print('run 0.25l')
#         # print('run 0.50l')
#         # print('run 0.75l')
#         print('run', i, 'lap')
#         laps += 1
#
# print('we run', laps, 'today')

# ### 4 CASE
# health = 5
# laps = 0
# weather = 'sun'
#
#
# for i in range(1, health + 1):
#     if weather == 'sun':
#         # print('run 0.25l')
#         # print('run 0.50l')
#         # print('run 0.75l')
#         print('run', i, 'lap')
#         laps += 1
#         if laps == 3:
#             break
#
# print('we run', laps, 'today')

# ############################
# # ### 5 CASE
# health = 5
# r_laps = 0
# weather = 'sun'
#
#
# while health != 0:
#     r_laps += 1
#     print('run', r_laps, 'lap')
#     health -= 1
#
# print('we run', r_laps, 'laps today')
#
# # ### 6 CASE # LOOOOOOOOOOOOOOOOOOOOP
# health = -5
# r_laps = 0
# weather = 'sun'
#
#
# while health != 0:
#     r_laps += 1
#     print('run', r_laps, 'lap')
#     health -= 1
#
# print('we run', r_laps, 'laps today')
#
# # ### 7 CASE #
# health = 5
# r_laps = 0
# weather = 'sun'
#
#
# while health > 0:
#     r_laps += 1
#     print('run', r_laps, 'lap')
#     health -= 1
#
# print('we run', r_laps, 'laps today')
#
# # ### 8 CASE #
# health = 5
# r_laps = 0
# weather = 'sun'
#
#
# while health > 0 and weather == 'sun':
#     r_laps += 1
#     print('run', r_laps, 'lap')
#     health -= 1
#     if health < 2:
#         break
#
# print('we run', r_laps, 'laps today')
#
#
#
# # ## 8 CASE #
# health = 5
# r_laps = 0
# weather = 'sun'
#
#
# while health > 0 and weather == 'sun':
#     r_laps += 1
#     print('run', r_laps, 'lap')
#     # DOPING ON 3 LAP
#     if r_laps == 3:
#         continue
#
#     health -= 1
#
#
# print('we run', r_laps, 'laps today')
#
# ### OR
#
# number = 0
# count = 0
# while count < 5:
#     number += 1
#     if (number % 2) == 1:
#         continue
#     print(number)
#     count += 1

### OR

# number = 0
# while number < 300:
#     number += 1
#     if number % 3 != 0:
#         continue
#     elif number % 5 != 0:
#         print(number, "divides by 3")
#     elif number % 7 != 0:
#         print(number, "divides by 3 and 5")
#     else:
#         print(number, "divides by 3 and 5 and 7")

# ## 9 CASE #
# health = 5
# r_laps = 0
# weather = 'sun'
#
#
# while health > 0 and weather == 'sun':
#     r_laps += 1
#     health -= 1
#     print('run', r_laps, 'lap')
#     if r_laps > 3:
#         weather = 'rain'
#
#
# print('we run', r_laps, 'laps today')

## 10 CASE #
#
# health = 5
# r_laps = 0
# weather = 'sun'
#
# while health > 0 and weather == 'sun':
#     r_laps += 1
#     health -= 1
#     print('run', r_laps, 'lap')
#     time.sleep(1)
#     if r_laps == 3:
#         weather = 'rain'
#         print('stop running. Rain')
#         time.sleep(5)
#     weather = 'sun'
#
#
# print('we run', r_laps, 'laps today')
# print('we have', health, 'health')


## 11 CASE #
# health = 5
# r_laps = 0
# weather = 'sun'
#
# while health > 0 and weather == 'sun':
#     r_laps += 1
#     health -= 1
#     print('run', r_laps, 'lap')
#     # time.sleep(1)
#     # if r_laps == 7:
#     #     weather = 'rain'
#     #     print('stop running. Rain')
#     #     # time.sleep(5)
#     # weather = 'sun'
# else:
#     print('Shower')
#
# print()
# print('we run', r_laps, 'laps today')
# print('we have', health, 'health')


## 12 CASE #
#
# health = 5
# r_laps = 0
# weather = 'sun'
#
# while health > 0 and weather == 'sun':
#     r_laps += 1
#     health -= 1
#     print('run', r_laps, 'lap')
#
#
#
#
# print()
# print('we run', r_laps, 'laps today')
# print('we have', health, 'health')

## 13 CASE #
#
# health = 85
# r_laps = 0
#
#
# while r_laps != 5:
#     step = 0
#     while step != 200:
#         step += 1
#         if step % 10 == 0:
#             health -= 1
#
#         if health == 0:
#             print('Im tired, I will rest a little')
#             health += 75
#
#     r_laps += 1
#     print('run', r_laps, 'lap')
#
#
# print()
# print('we run', r_laps, 'laps today')
# print('we have', health, 'health')
## 14 CASE #

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end="\t")
#     print("\n")


# try:
#     a = input("Введите первое число: ")
#     b = input("Введите второе число: ")
#     print("Результат: ", int(a)/int(b))
# except ValueError:
#     print("Пожалуйста, вводите только числа")
# except ZeroDivisionError:
#     print("На ноль делить нельзя")


# try:
#     a = input("Введите первое число: ")
#     b = input("Введите второе число: ")
#     result = int(a)/int(b)
# except (ValueError, ZeroDivisionError):
#     print("Что-то пошло не так...")
# else:
#     print("Результат в квадрате: ", result**2)


# -*- coding: utf-8 -*-

# try:
#     a = input("Введите первое число: ")
#     b = input("Введите второе число: ")
#     result = int(a)/int(b)
# except (ValueError, ZeroDivisionError):
#     print("Что-то пошло не так...")
# else:
#     print("Результат в квадрате: ", result**2)
# finally:
#     print("Вот и сказочке конец, а кто слушал - молодец.")


# while True:
#     a = input("Введите число: ")
#     b = input("Введите второе число: ")
#     try:
#         result = int(a)/int(b)
#     except ValueError:
#         print("Поддерживаются только числа")
#     except ZeroDivisionError:
#         print("На ноль делить нельзя")
#     else:
#         print(result)
#         break

# try:
#     apples = int(input("Enter the amount of apples you have: "))
#     if apples < 0:
#         raise Exception
#     print("You have", apples, "apples")
# except Exception:
#     print("You can’t have", apples, "apples")

# try:
#     raise ValueError
# except ValueError:
#     print("Improper value was obtained")
# except Exception:
#     print("Hmm... Something went wrong")


# try:
#     v1 = int(input("Enter the amount of received items: "))
#     # items_type = input("Specify the type of received items: ")
#     v2 = int(input("Enter the number of parts: "))
#     v3 = v1 / v2
#     print("Supply of", v3, "saved")
#     print("Each of", v1, "parts consists of", v2)
# except (ValueError, ZeroDivisionError):
#     print("Improper value was obtained")

# for i in range(1, 10):
#     print('1')
#     for j in range(1, 10):
#         print('\t2')
#         for j in range(1, 10):
#             print('\t\t3')
    #print()


# A = [[20, 4, 9],
#      [1, 9, 87],
#      [22, 56, 0]]
#
# for row in A:
#     for elen in row:
#         print(elen, end='\t|')
#     print()


a = [1, 2, 3]
b = a
b[0] = 5
print(a, b)

a = [1, 2, 3]
b = a.copy()
b[0] = 5
print(a, b)

# CASE 1
a = [1, 2, [3, 4, 5]]
b = a.copy()
b[2][0] = 10
print(a, b)


from copy import deepcopy

a = [1, 2, [3, 4, 5]]
b = deepcopy(a)
b[2][0] = 10
print(a, b)
