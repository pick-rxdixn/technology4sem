def input_list():
    print("Введите элемент: ")
    i = 0
    while (i < n):
        tmp = int(input(""))
        arr.append(tmp)
        i += 1


def output_list():
    print("Список: ")
    i = 0
    while (i < n):
        print(arr[i], end=" ")
        i += 1

arr = list()
i = True
n = int(input("Введите количество элементов: "))
if n < 0:
    print("Минимум 0 элементов")
    exit()



input_list()
output_list()
print("")