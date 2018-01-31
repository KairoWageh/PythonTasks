def stars(number):
    i = 1
    for i in range(number+1):
        x = number - i
        print(" " * x + "*" * i)
        i += 1
stars(4)
