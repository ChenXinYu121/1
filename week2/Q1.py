
tel = input("请输入您的手机号：")

list1 = [138, 134, 135, 139, 159, 158]

try:

    int(tel)

    if (len(tel) == 11):

        head = tel[0:3]
        bool = False

        for i in list1:
            if (int(head) == (i)):
                bool = True
                break
        if bool:
                print("手机号码有效")
        else:
                print("手机号无效")

    else:
        print("输入手机号无效")

except ValueError:
    print("输入手机号无效")