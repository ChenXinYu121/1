
for x in range(1,10):
    for y in range(1,10):
        if x >= y:
            print(str(y) + "*" + str(x) + "=" + str(x*y) +"     ", end='')
    print()
