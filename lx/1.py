import random

num = random.randint(1, 100)


while True:
    shu = int(input("请输入一个正整数(0~100)："))

    if shu == num:
        print("恭喜你猜中啦，你真棒")
        break
    elif shu > num:
        print("你猜大了")
    elif shu < num:
        print("你猜小了")