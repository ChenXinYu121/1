
a = []

for i in range(100,201):

    b = 0

    for x in range(2,i-1):
        if i % x == 0:
            b += 1
    if b == 0:
        a.append(i)

print(a)
print(len(a))
