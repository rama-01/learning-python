def get_max2(nums):
    m1, m2 = (nums[0], nums[1]) if nums[0] > nums[1] else (nums[1], nums[0])
    for i in range(2, len(nums)):
        if nums[i] > m1:
            m2 = m1
            m1 = nums[i]
        elif nums[i] > m2:
            m2 = nums[i]
    return m1, m2
    # 在python中，逗号,被视作元组的标志符号，因此4,5本质上就是一个元组


print(get_max2([2, 1, 3, 5, 4]))
