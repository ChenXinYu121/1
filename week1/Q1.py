
tel = input("请输入您的手机号:")

list1 = [159, 158, 138, 134, 135]

try:
    int(tel)

    if (len(tel) == 11):

        head = tel[0:3]

        bool = False

        for i in list1:
            if(int(head) == i):
                bool = True
                break
        if bool:
                print("手机号符合")
        else:
                print("不符合")


    else:
        print("输入手机号不符合")
except ValueError:
    print("手机号不符合")