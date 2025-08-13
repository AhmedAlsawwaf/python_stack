x = [[5,2,3],[10,8,9]]
student =[
    {'first_name' : 'Michael' , 'last_name' : 'Jordan'},
    {'first_name' : 'John' , 'last_name' : 'Rosales'}
]
sports_directory={
    'basketball' : ['Kobe' , 'Jordan' , 'James' , 'Curry'],
    'soccer' : ['Messi' , 'Ronaldo' , 'Rooney']
}
z = [{'x': 10 , 'y': 20}]

# 1
print("******1********")
x[1][0]=15
student[0]['last_name'] = 'Bryant'
sports_directory['soccer'][0] = 'Andres'
z[0]['y'] =30
print(z)


#3,4 
students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
def iterateDictionary(lst):
    for i in lst:
        for x,y in i.items():
            print(f'{x} - {y}')
iterateDictionary(students)

# 5,6
def iterateDictionary2(key, lst):
    for item in lst:
        print(item[key])
iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)

# 7,8
def printInfo(info):
    for key,value in info.items():
        print(f'\n{len(value)} {key.upper()}')
        for i in value:
            print(i)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)