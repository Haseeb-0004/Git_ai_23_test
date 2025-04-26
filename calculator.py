print("This is Bug Hunter Practically!")
print("Testing will help me find bugs that users might encounter")

class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero") # Bug: returns string instead of raising exception
        return a / b
    
    def power(self, a, b):
        if b < 0:
            return 1 / (a ** abs(b)) # Bug: incorrect handling of negative exponents
        return a ** b
    
    def factorial(self, n):
        """Calculate the factorial of n"""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        
        if n == 0:
            return 1

        return n * self.factorial(n-1)
        
    def fibonacci(self, n):
        """Calculate the nth Fibonacci number"""
        if n < 0:
            raise ValueError("Fibonacci is not defined for negative numbers")
        
        if n == 0:
            return 0
        
        elif n == 1:
            return 1
        
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)
