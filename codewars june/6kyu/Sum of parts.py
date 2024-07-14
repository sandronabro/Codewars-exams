def parts_sums(ls):
    old_sum = sum(ls)
    result = []
    new_sum = 0
    
    for i in ls:
        result.append(old_sum - new_sum)
        new_sum += i
    result.append(0)
    
    return result