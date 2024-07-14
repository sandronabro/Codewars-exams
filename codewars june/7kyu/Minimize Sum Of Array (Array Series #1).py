def min_sum(arr):
    arr.sort()
    x = len(arr)
    minimum_sum = 0
    
    for i in range(x // 2):
        minimum_sum += arr[i] * arr[x - 1 - i]
        
    return minimum_sum