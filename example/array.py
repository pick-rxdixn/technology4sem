arr = list()
i = True
while i:
    n = int(input("Введите количество элементов: "))
    if n > 15:
        print("Максимум 15 элементов")
    else:
        i = False
print("Введите элемент: ")
i = 0
while (i < n):
    tmp = int(input(""))
    arr.append(tmp)
    i += 1

print("Список: ")
i = 0
while (i < n):
    print(arr[i], end = " ")
    i += 1
print("")