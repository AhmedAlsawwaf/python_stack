class Underscore:
    def map(self, iterable, callback):
        return [callback(item) for item in iterable]
    
    def find(self, iterable, callback):
        for item in iterable:
            if callback(item):
                return item
        return None
    
    def filter(self, iterable, callback):
        return [item for item in iterable if callback(item)]
    
    def reject(self, iterable, callback):
        return [item for item in iterable if not callback(item)]

_ = Underscore()

numbers = [1, 2, 3, 4, 5, 6]

squares = _.map(numbers, lambda x: x ** 2)
print(squares)

first_even = _.find(numbers, lambda x: x % 2 == 0)
print(first_even) 

all_evens = _.filter(numbers, lambda x: x % 2 == 0)
print(all_evens)

all_odds = _.reject(numbers, lambda x: x % 2 == 0)
print(all_odds)  

