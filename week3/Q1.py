tel = input("请输入您的手机号:")

list = [138, 134, 139, 159, 158, 134]

try:

    int(tel)

    if (len(tel) == 11):

        head = tel[0:3]
        bool = False

        for i in list:

            if (int(head) == (i)):
                bool = True
                break
        if bool:
            print("输入手机号有效")
        else:
            print("输入手机号无效")

except ValueError:
    print("输入手机号无效")