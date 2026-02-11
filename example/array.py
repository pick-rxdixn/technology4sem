arr = list()
n = int(input("Введите количество элементов: "))
print("Введите элемент: ")
i = 0
while (i < n):
    tmp = int(input(""))
    arr.append(tmp)
    i += 1
print("Список:")
i = 0
while (i < n):
    print(arr[i], end = " ")
    i += 1
print("")
