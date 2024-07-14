def dating_range(age):
    if age <= 14:
        equation1 = (age - 0.10 * age)
        equation2 = (age + 0.10 * age)
    else:
        equation1 = (age / 2) + 7
        equation2 = (age - 7) * 2
    
    return "{}-{}".format(int(equation1), int(equation2))