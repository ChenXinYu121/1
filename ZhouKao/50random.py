import random
#50个随机数
list1 = ""
list2 = ""

for i in range(1, 51):

    num = random.randrange(-10, 10)

    if num >= 0:

        list1 += num

    elif num < 0:

        list2 += num

    print(num)




