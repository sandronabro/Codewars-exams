def smaller(arr):
    result = []
    for i in range(len(arr)):
        counter = 0
        for x in range(i+1,len(arr)):
            if arr[x] < arr[i]:
                counter+=1
        result.append(counter)
    return result