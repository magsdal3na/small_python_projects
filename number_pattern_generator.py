def number_pattern(n):

    if type(n) != int:
        return 'Argument must be an integer value.'
    elif n <= 0:
        return 'Argument must be an integer greater than 0.'
    
    result = ' '.join(str(int(i)) for i in range(1, (n + 1)))
    return result
    

print(number_pattern(4))
print(number_pattern(12))
