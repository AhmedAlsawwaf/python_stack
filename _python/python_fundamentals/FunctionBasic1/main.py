# 1
print("snippet 1 is equal to :")
def a():
    return 5
print (a())

# 2
print("snippet 2 is equal to :")
def a():
    return 5
print (a()+a())

# 3
print("snippet 3 is equal to :")
def a():
    return 5
    return 10
print(a())

# 4
print("snippet 4 is equal to :")
def a():
    return 5
    print(10)
print(a())

#5
print("snippet 5 is equal to :")
def a():
    print(5)
x = a()
print(x)

#6
print("snippet 6 is equal to :")
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))

#7
print("snippet 7 is equal to :")
def a(b,c):
    return str(b) + str(c)
print(a(2,5))

# 8
print("snippet 8 is equal to :")
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

# 9
print("snippet 9 is equal to :")
def a(b,c):
    if b < c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

# 10
print("snippet 10 is equal to :")
def a(b,c):
    return b+c
    return 10
print(a(3,5))

# 11
print("snippet 11 is equal to :")
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

# 12
print("snippet 12 is equal to :")
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

# 13 
print("snippet 13 is equal to :")
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
b = a()
print(b)

# 14
print("snippet 14 is equal to :")
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

# 15
print("snippet 15 is equal to :")
def a():
    print(1)
    x =b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

def x(name ="" ,num = 2):
    return