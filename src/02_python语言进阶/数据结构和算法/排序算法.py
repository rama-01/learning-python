def select_sort(items, comp=lambda x, y: x < y):
    # 复制items
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items

res = select_sort([12, 0, 1, -2, 12, -100])
print(res)