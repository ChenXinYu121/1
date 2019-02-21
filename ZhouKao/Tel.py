
#手机号判断

tel = int(input("请输入您的手机号:"))

if (type(tel)) == int:
    print("输入的是数字")
    if tel % 10000000000 > 0 :
        print("手机号长度满足")

    else:
        print("长度不满足条件")
else:
    print("输入的不是数字")