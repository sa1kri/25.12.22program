import time

def layer(Wide, SymbolPosition, Symbol=' '):
        print("|", end='')
        for i in range(SymbolPosition):
            print(" ", end='')
        print(Symbol, end='')
        for i in range(Wide-SymbolPosition):
            print(" ", end='')
        print("|")
    
def animation(Wide,Symbol,Cells,Duration=1):
    SymbolPositionX = 0
    SymbolPositionY = 0
    IncDecRow = 1
    IncDecCol = 1
    while Duration:
        for i in range(Wide):
            for j in range(Cells):
                if SymbolPositionY == j:
                    layer(Wide, SymbolPositionX, Symbol)
                    SymbolPositionX += IncDecRow
                else:
                    layer(Wide, SymbolPositionX)
                if SymbolPositionX == Wide:
                    IncDecRow = -1
                elif SymbolPositionX == 0:
                    IncDecRow = 1
                if SymbolPositionY == Cells-1:
                    IncDecCol = -1
                elif SymbolPositionY == 0:
                    IncDecCol = 1
            SymbolPositionY += IncDecCol    
            time.sleep(.05)  
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")  
Wide = int(input("Широкий спектр полей: "))
Symbol = input("Символ: ")
NumOfCell = int(input("Количество ячеек: "))
if Wide < 1 or Symbol == '' or NumOfCell < 1:
    print("Свойство символа количества ячеек в широком поле равно нулю")
else:
    Duration = int(input("Продолжительность анимации или нет для цикла: "))
    if Duration:
        animation(Wide, Symbol, NumOfCell, Duration)
    else:
        animation(Wide, Symbol, NumOfCell)