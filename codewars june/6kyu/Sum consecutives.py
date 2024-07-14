def sum_consecutives(lst):
    result = []
    new_sum = lst[0]
    
    for i in range(1, len(lst)):
        if lst[i] == lst[i-1]:
            new_sum += lst[i]
        else:
            result.append(new_sum)
            new_sum = lst[i]
            
    result.append(new_sum)
    
    return result