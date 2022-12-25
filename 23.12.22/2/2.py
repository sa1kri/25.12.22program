def graphic(argArr, SortType=0):
    argArr.sort()
    if SortType:
        argArr = argArr[::-1]
    for i in argArr:
        for j in range(i):
            print("#", end='')
        print(i)
NumOfArgs = int(input("Количество аргументов: "))
print("Введите аргументы ")
argArr = [int(input()) for i in range(NumOfArgs)]
SortType = input("типы сортировки: 1 - по убыванию, узел - по возрастанию: ")
if SortType:
    graphic(argArr, SortType)
else:
    graphic(argArr)