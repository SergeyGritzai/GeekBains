# 1 Task
#Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах
my_time = int(input('Введите время: '))
print((my_time // 86400), ' дн. ', (my_time % 86400) // 3600, ' ч. ', (my_time % 3600) // 60, ' мин. ', my_time % 60, ' c.')



# 2 Task
cubes = [x**3 for x in range(1000) if x % 2 != 0]

final_numbers_sum = 0
# проход по списку
for num in cubes:
    numbers_sum = 0
    for i in str(cubes):
        numbers_sum += int(numbers_sum)
    if numbers_sum % 7 == 0:
        final_numbers_sum += num
print(final_numbers_sum)


cubes = [x**3 + 17 for x in range(1000) if x % 2 != 0]

final_numbers_sum = 0
# проход по списку
for num in cubes:
    numbers_sum = 0
    for i in str(cubes):
        numbers_sum += int(numbers_sum)
    if numbers_sum % 7 == 0:
        final_numbers_sum += num
print(final_numbers_sum)

# 3 Task
percent = int(input('Введите число: '))
if percent == 1:
    word = 'процент'
elif percent <= 4:
    word = 'процента'
else:
    word = 'процентов'
print(percent, word)