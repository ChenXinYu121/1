
import random

list = []

for i in range(50):

    num = random.choice(range(-10,11))
    list.append(num)
z = []
f = []
for i in list:
    if i < 0:
        z.append(i)
    elif i > 0:
        f.append(i)

print("正数有：", z)
print("负数有：", f)

