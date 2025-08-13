# 1.countdown
def countdown(num):
    list =[]
    for x in range(num,0,-1):
        list.append(x)
    return list
print(countdown(5))

# 2.print and return
def print_and_return(numbers):
    print(numbers[0])
    return numbers[1]
print(print_and_return([1,2]))

# 3.first plus length
def first_plus_length(numbers):
    return numbers[0] + len(numbers)
print(first_plus_length([1,2,3,4,5,6]))

# 4.values grater than second
def values_greater_than_second(lst):
    if len(lst) < 2:
        return False
    
    second_val = lst[1]
    new_list = []
    count = 0
    
    for num in lst:
        if num > second_val:
            new_list.append(num)
            count += 1
    
    print(count)
    return new_list
print(values_greater_than_second([9,4,2,3,4,5,6,7]))

# 5.This Length, That Value
def length_and_value(size, value):
    return [value] * size
print(length_and_value(7,7))