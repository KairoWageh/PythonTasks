#list to store each number multiplication
#numbers = []
# list to store the results in
#table = []

#  3
# Output     [[1], [2, 4], [3, 6, 9]]
# my output [[1, 2, 4, 3, 6, 9], [1, 2, 4, 3, 6, 9], [1, 2, 4, 3, 6, 9]]
#while inner <= number:
#    mult = 1
#    numbers.append(mult*inner)   # m1 i1  m2 i1 m2 i2   m1 i3  m2 i3    m3 i3
#    mult += 1
#    while mult <= inner:
#        numbers.append(mult*inner)
#        mult += 1
#    inner += 1
#    table.append(numbers)
#print(table)



def multiplication(number):
    inner = 1
    mult = 1
    table = []
    for inner in range(number):
        numbers = []
        inner += 1
        for mult in range(inner):
            mult+=1
            numbers.append(inner*mult)
        table.append(numbers)
    return table
print(multiplication(2))
