# Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность
# и содержащие максимальное количество элементов.

def list_filter(list_of_num):
    result = []
    for j in range(0, len(list_of_num)):
        k = 0
        new_list = [list_of_num[j]]
        for i in range(j + 1, len(list_of_num)):
            if list_of_num[i] > new_list[k]:
                new_list.append(list_of_num[i])
                k += 1
        result.append(new_list)

    for i in range(0, len(result)):
        temp = [0]
        for j in range(0, len(list_of_num)):
            if list_of_num[j] == result[i][0]:
                break
            if result[i][0] > list_of_num[j] > temp[-1]:
                temp.append(list_of_num[j])
        temp.remove(0)
        result[i] = temp + result[i]
    result = sorted(result, key=len)
    return result[-1]


first_list = [1, 5, 2, 3, 4, 6, 1, 7]

res = list_filter(first_list)
print(res)
