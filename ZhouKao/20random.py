import random
#20随机数
list1 = []
for i in range(0, 20):

    list1 = random.randrange(0,100)
    if i % 2 == 0:
        print("-----------------------------")
        print(list1)