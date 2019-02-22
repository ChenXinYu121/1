num = int(input("请输入一个数："))

p = 1

for i in range(1,num+1):

    p = p * i

print(num, "的阶乘结果为：", p)