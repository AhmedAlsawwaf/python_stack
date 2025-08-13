# 1.biggie size 
def biggie_size(lst):
    for i in range(len(lst)):
        if lst[i] > 0:
            lst[i] = "big"
    return lst
print(biggie_size([1,-1,2,-2,3,-3,4,5,-6]))

# 2.count positives
def count_positives(lst):
    total = 0
    for i in  lst:
        if i > 0:
            total += i
    lastIndex = len(lst) -1
    lst[lastIndex] = total
    return lst
print(count_positives([1,2,3,4,-1,-5,1,0,0]))

# 3.Average
def average(lst):
    sum = 0
    for i in lst:
        sum += i
    avg = sum/len(lst)
    return avg
print(average([1,2,3,4,5,6,7,8,9,10]))

# 4.length
def length(lst):
    return len(lst)
print(length([]))

# 5.Minimum
def minimum(lst):
    if len(lst) < 1:
        return  False
    minValue = lst[0]
    for i in lst:
        if i < minValue:
            minValue = i
    return minValue
print(minimum([1,2,3,4,5,6,-1,21,4,4,5,-9,1,1]))

# 6.Maximum
def maximum(lst):
    if len(lst) < 1:
        return  False
    maxValue = lst[0]
    for i in lst:
        if i > maxValue:
            maxValue = i
    return maxValue
print(maximum([1,2,3,4,5,6,-1,21,4,4,5,-9,1,1]))
# total function
def total(lst):
    total = 0
    for i in lst:
        total += i
    return total
print(total([1,2,3,4,5,6,-1,21,4,4,5,-9,1,1]))

# 7.Ultimate Analysis
def ultimate_analysis(lst):
    if len(lst) < 1:
        return  False
    return {
        'Total': total(lst),
        'Average': average(lst),
        'Minimum': minimum(lst),
        'Maximum': maximum(lst),
        'Length': length(lst)
    }
print(ultimate_analysis([1,2,3,4,5,6,-1,21,4,4,5,-9,1,1]))

# 8.reverse list 
def reverse_list(lst):
    for x in range (len(lst)//2):
       lst[x],lst[-1-x] = lst[-1-x],lst[x]
    return lst
print(reverse_list([1,2,3,4,5,6,-1,21,4,4,5,-9,1,1]))