""""
输入M，N，计算C(M,N)
"""
m = int(input('m='))
n = int(input('n='))

fm = 1
for m in range(1, m + 1):
    fm *= m

fn = 1
for n in range(1, 1 + n):
    fn *= n

fmn = 1
for k in range(1, m - n + 1):
    fmn *= k

print('total combination counts is %d' % (fm // fn // fmn))


# refactor

def factor(num):
    res = 1
    for n in range(1, num + 1):
        res *= n
    return res


m = int(input('m='))
n = int(input('n='))

print(factor(m) // factor(n) // factor(m - n))
