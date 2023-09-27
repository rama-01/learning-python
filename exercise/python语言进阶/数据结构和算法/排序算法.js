//实现一个排序算法
function sort(array, comp = (x, y) => x < y) {
    const arr = [...array]
    for (let i = 0; i <
    arr.length - 1; i++
    ) {
        min_index = i
        for (let j = i + 1; j < arr.length; j++) {
            if (comp(arr[j], arr[min_index])) {
                min_index = j
            }
        }
        [arr[min_index], arr[i]] = [arr[i], arr[min_index]]
    }
    return arr
}

res = sort([12, 1, 2])
console.log(res)