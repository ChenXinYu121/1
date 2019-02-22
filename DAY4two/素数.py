#素数

b = 0

for i in range(100,201):
    k = 0

    for j in range(2,i):
        if i % j == 0:
            k += 1

    if k == 0:

        print(i)
        b += 1

print(b)