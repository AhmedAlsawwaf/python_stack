class Animal:
    def __init__(self,animal_name,age,health_level ,happy_level):
        self.name = animal_name
        self.age = age
        self.health_level = health_level
        self.happy_level = happy_level
    def display_info(self):
        print(f"The {self.name} health level is: {self.health_level} while his happy level is {self.happy_level}")
        return self
    def feed(self):
        self.health_level += 10
        self.happy_level += 10
        return self
    
class Lions(Animal):
    def __init__(self, animal_name, age, health_level =50, happy_level =50 ,color = "Yellow"):
        super().__init__(animal_name, age, health_level, happy_level)
        self.color = color
    
    def feed(self):
        self.health_level +=10
        return self

class Bears(Animal):
    def __init__(self, animal_name, age, health_level = 40, happy_level = 40,area ="Pole"):
        super().__init__(animal_name, age, health_level, happy_level)
        self.area = area
    
class Monkeys(Animal):
    def __init__(self, animal_name, age, health_level = 70, happy_level = 70,monkey_type ="Capuchin"):
        super().__init__(animal_name, age, health_level, happy_level)
        self.monkey_type = monkey_type
    def feed(self):
        self.happy_level +=10
        return self

class Zoo:
    def __init__(self,zoo_name):
        self.zoo_name =zoo_name
        self.animals = {}
    def add_lion(self,name,age):
        self.animals[name]=Lions(name,age)
        return self
    def add_bear(self,name,age):
        self.animals[name]=Bears(name,age)
        return self
    def add_monkey(self,name,age):
        self.animals[name]=Monkeys(name,age)
        return self
    def print_all_info(self):
        print("*"*30,self.zoo_name,"*"*30)
        for value in self.animals.values():
            value.display_info()
        return self

# testing
zoo1 = Zoo("Ahmed's Zoo")
zoo1.add_bear("Alex",15)
zoo1.add_bear("Neal",17)
zoo1.add_lion("Leo",20)
zoo1.add_lion("Semba",22)
zoo1.add_monkey("Loca",12)
zoo1.add_monkey("Max",10)
zoo1.print_all_info()