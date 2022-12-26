import time
def animation(Wide,Symbol,Duration=1):
    SymbolPosition = 0
    IncDec = 1
    while Duration:
        for i in range(Wide):
            print("|", end='')
            for i in range(SymbolPosition):
                print(" ", end='')
            print(Symbol, end='')
            for i in range(Wide-SymbolPosition):
                print(" ", end='')
            print("|")
            SymbolPosition += IncDec
            time.sleep(.05)
        if IncDec == 1:
            IncDec = -1
        else:
            IncDec = 1
Wide = int(input("Размер поля: "))
Symbol = input("Символ: ")

if Wide < 1 or Symbol == '':
    print("Свойство широкого поля или символов равно нулю")
else:
    Duration = int(input("Бесконечная анимация (1) или нет  (0): "))
    if Duration:
        animation(Wide, Symbol, Duration)
    else:
        animation(Wide, Symbol)

