# -- coding:utf-8 --
'''
题目：求s=a+aa+aaa+aaaa+aa…a的值，其中a是一个数字。例如2+22+222+2222+22222(此时 
　　　共有5个数相加)，几个数相加有键盘控制。 
'''
Tn = 0
Sn = []

n = int(input('n = '))
a = int(input('a = '))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print(Tn)

print(Sn)
b = sum(Sn)
print('sun = %d' % b)