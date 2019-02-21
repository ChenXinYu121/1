def jc(n):
    if n <= 1:
        return n
    if n != 1:
        n *= jc(n-1)
        return n
print('请输入数字')
n=int(input())
sum = 0
while n > 0:
    b = jc(n)
    n -= 1
    sum += b
print('阶乘和是', sum)
