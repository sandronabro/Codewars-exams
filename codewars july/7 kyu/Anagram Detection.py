# write the function is_anagram
def is_anagram(test, original):
    test = test.replace(" ", "").lower()
    original = original.replace(" ", "").lower()
    
    if len(test) != len(original):
        return False
    
    result = {}
    for char in test:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
        
    for char in original:
        if char in result:
            result[char] -= 1
        else:
            return False
        
    for value in result.values():
        if value != 0:
            return False
        
    return True