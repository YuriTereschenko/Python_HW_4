# Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию.
import random


def fill_file(length):
    rnd_nums = []
    for i in range(0, length):
        rnd_nums.append(random.randint(0, 999))
    with open("t1.txt", "w") as file:
        for i in rnd_nums:
            file.write(f"{i} ")
    file.close()


def array_sort(way):
    with open(way, 'r') as arr:
        num = arr.read()
        arr.close()
    num = num.split()
    for i in range(0, len(num)):
        num[i] = int(num[i])
    num.sort()
    with open(way, 'w') as arr:
        for i in num:
            arr.write(f'{str(i)} ')
    arr.close()


fill_file(6)
array_sort("t1.txt")
