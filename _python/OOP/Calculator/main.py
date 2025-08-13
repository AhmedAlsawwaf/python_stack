from numbers import Number
class Calculate:
    def __init__(self, x: Number, y: Number):
        if not isinstance(x, Number) or not isinstance(y, Number):
            raise ValueError("Both arguments must be numbers")
        self.first_num = x
        self.sec_num = y
    
    def add(self):
        return self.first_num + self.sec_num
    
    def mult(self):
        return self.first_num * self.sec_num
    
    def sub(self):
        return self.first_num - self.sec_num

    def divide(self):
        if self.sec_num == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self.first_num / self.sec_num
    
try:
    first_equation = Calculate(10, 20)
    sec_equation = Calculate(20, -50)
    third_equation = Calculate(20, 0)
    fourth_equation = Calculate(2, "A") # this will give : Input error: Both arguments must be numbers
    
    print(first_equation.add())
    print(first_equation.mult())
    print(first_equation.sub())
    print(first_equation.divide())

    print(sec_equation.add())
    print(sec_equation.mult())
    print(sec_equation.sub())
    print(sec_equation.divide())

    print(third_equation.add())
    print(third_equation.mult())
    print(third_equation.sub())
    print(third_equation.divide()) # this will give :Math error: Cannot divide by zero

except ValueError as e:
    print(f"Input error: {e}")
except ZeroDivisionError as e:
    print(f"Math error: {e}")