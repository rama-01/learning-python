# 此问题可以抽象为总数为 7 个空隙，选择的个数为 3 个隔板
def divide_apples(apples, groups, min_per_group, current_groups, current_total):
    if current_groups == groups - 1:
        if apples >= min_per_group:
            current_total += 1
        return current_total
    for i in range(min_per_group, apples - (groups - current_groups - 1) * min_per_group + 1):
        current_total = divide_apples(apples - i, groups, min_per_group, current_groups + 1, current_total)
    return current_total


apples = 8
groups = 4
min_per_group = 1
total_solutions = divide_apples(apples, groups, min_per_group, 0, 0)
print(total_solutions)
