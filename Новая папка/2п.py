result = []
row = True

while row:
    row = input()
    if row:
        numbers = map(int, row.split())
        result.append(list(numbers))
        
print(result)