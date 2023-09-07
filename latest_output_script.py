class AdvancedCalculator:

    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "You can't divide by zero!"
        return a / b

    def power(self, a, b):
        return a ** b

    def root(self, a, b):
        if b == 0:
            return "You can't do a zero root!"
        return a ** (1.0 / b)

    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n-1)

if __name__ == "__main__":
    calc = AdvancedCalculator()
    print(calc.add(2, 2))
    print(calc.subtract(2, 2))
    print(calc.multiply(2, 2))
    print(calc.divide(2, 2))
    print(calc.power(2, 2))
    print(calc.root(2, 2))
    print(calc.factorial(5))