import math

apples = 8
groups = 4


# 计算组合数
def combination(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


# 计算总方案数量
total_solutions2 = combination(apples - 1, groups - 1)
print(total_solutions2)