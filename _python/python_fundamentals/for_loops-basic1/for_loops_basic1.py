# Basic
for x in range (151):
    print(x)

# Multiplies by 5 
# 1- using %
for x in range (5,1001):
    if (x % 5 == 0):
        print(x)
# 2- using +5
for x in range (5,1001,5):
    print(x)

# Counting the dojo way
for x in range (1,101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x)

# Whoa, That Sucker's Huge
total = 0
for x in range(1,500000,2):
    total +=x
print(total)

# Countdown by 4
for x in range(2018,0,-4):
    print(x)

# Flexible Counter
lowNum = 0
highNum = 9
mult = 3
for x in range(lowNum,highNum+1):
    if x % mult ==0:
        print(x)