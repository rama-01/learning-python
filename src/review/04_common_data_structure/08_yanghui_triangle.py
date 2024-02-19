def yh_triangle():
    row = int(input('please input rows:'))
    yh = [[]] * row
    for r in range(row):
        yh[r] = [None] * (r + 1)
        for l in range(len(yh[r])):
            if l == 0 or r == l:
                yh[r][l] = 1
            else:
                yh[r][l] = yh[r - 1][l] + yh[r - 1][l - 1]
            print(yh[r][l], end='\t')
        print()


yh_triangle()
