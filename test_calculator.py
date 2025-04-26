# import pytest
# from calculator import Calculator

# def test_add():
#     calc = Calculator()
#     assert calc.add(3, 5) == 8
#     assert calc.add(-1, 1) == 0
#     assert calc.add(-1, -1) == -2

# def test_subtract():
#     calc = Calculator()
#     assert calc.subtract(5, 3) == 2
#     assert calc.subtract(1, 5) == -4
#     assert calc.subtract(-5, -3) == -2

# def test_multiply():
#     calc = Calculator()
#     assert calc.multiply(5, 3) == 15
#     assert calc.multiply(2, -6) == -12
#     assert calc.multiply(-5, -3) == 15
#     assert calc.multiply(-5, 0) == 0
#     assert calc.multiply(3.6, 3.0) == 10.8
#     assert calc.multiply(7.0, -2.5) == -17.5
    

# def test_divide():
#     calc = Calculator()
#     # Normal Division
#     assert calc.divide(15, 3) == 5
#     assert calc.divide(-6, 2) == -3
#     # Division with decimals
#     assert calc.divide(5, 2) == 2.5
#     assert calc.divide(9, -2) == -4.5
#     with pytest.raises(ValueError):
#         assert calc.divide(2, 0) == 0
#         assert calc.divide(0, 3) == 0


# #-----------------------------------------------------------#
# import pytest
# # from calculator import Calculator

# @pytest.mark.parametrize("a, b, expected", [
#     (3, 5, 8),
#     (-1, 1, 0),
#     (-1, -1, -2),
#     (0, 0, 0)
# ])

# def test_add_parameterized(calculator, a, b, expected):
#     # calc = Calculator()
#     assert calculator.add(a, b) == expected

# #-----------------------------------------------------------#
# @pytest.mark.parametrize("a, b, expected", [
#     (5, 3, 2),
#     (1, 5, -4),
#     (-5, -3, -2),
#     (0, 0, 0)
# ])

# def test_subtract_parameterized(calculator, a, b, expected):
#     # calc = Calculator()
#     assert calculator.subtract(a, b) == expected

# #-----------------------------------------------------------#
# @pytest.mark.parametrize("a, b, expected", [
#     (3, 5, 15),
#     (2, -6, -12),
#     (-5, -3, 15),
#     (-5, 0, 0),
#     (3.6, 3.0, 10.8),
#     (7.0, -2.5, -17.5)
# ])

# def test_multiply_parameterized(calculator, a, b, expected):
#     # calc = Calculator()
#     assert calculator.multiply(a, b) == expected

# #-----------------------------------------------------------#
# @pytest.mark.parametrize("a, b, expected", [
#     (15, 3, 5),
#     (-6, 2, -3),
#     (5, 2, 2.5),
#     (9, -2, -4.5),
# ])

# def test_divide_parameterized(calculator, a, b, expected):
#     # calc = Calculator()
#     assert calculator.divide(a, b) == expected

# def test_divide_by_zero(calculator):
#     # calc = Calculator()
#     with pytest.raises(ValueError):
#         calculator.divide(2, 0)
#         calculator.divide(0, 3)

# #-----------------------------------------------------------#
# @pytest.mark.parametrize("a, b, expected", [
#     (2, 3, 8),
#     (3, 2, 9),
#     (2, 0, 1),
#     (2, -2, 0.25), # Should be 1/(2^2) = 0.25
#     (10, -1, 0.1) # Should be 1/10 = 0.1
# ])
# def test_power_parameterized(calculator, a, b, expected):
#     assert calculator.power(a, b) == pytest.approx(expected)

# #-----------------------------------------------------------#
# @pytest.mark.parametrize("n, expected", [
#     # Edge Cases
#     (0, 1),
#     (1, 1),
#     # Normal Cases
#     (2, 2),
#     (3, 6),
#     (5, 120),
#     (7, 5040),
# ])
# def test_factorial(calculator, n, expected):
#     assert calculator.factorial(n) == expected

# def test_factorial_negative(calculator):
#     with pytest.raises(ValueError): # Error Cases
#         calculator.factorial(-3)

# #-----------------------------------------------------------#
# @pytest.mark.parametrize("n, expected", [
#     # Edge Cases
#     (0, 0),
#     (1, 1),
#     # Normal Cases
#     (2, 1),
#     (3, 2),
#     (5, 5),
#     (7, 13),
#     (10, 55),
# ])
# def test_fibonacci(calculator, n, expected):
#     assert calculator.fibonacci(n) == expected

# def test_fibonacci_negative(calculator):
#     with pytest.raises(ValueError): # Edge Cases
#         calculator.fibonacci(-5)

# #-----------------------------------------------------------#

# def test_precise_addition(precise_calculator):
#     assert precise_calculator.add(1.2345, 2.3456) == 3.58

# def test_precise_subtraction(precise_calculator):
#     assert precise_calculator.subtract(5.6789, 2.3456) == 3.33

# def test_precise_multiplication(precise_calculator):
#     assert precise_calculator.multiply(1.2345, 2.3456) == 2.9

# def test_precise_division(precise_calculator):
#     assert precise_calculator.divide(5.6789, 2.3456) == 2.42

# def test_precise_power(precise_calculator):
#     assert precise_calculator.power(2.3456, 2) == 5.5

# #-----------------------------------------------------------#

import pytest
from conftest import PreciseCalculator

@pytest.mark.parametrize("precision, a, b, expected", [
    (0, 1.2345, 2.3456, 4.0),    
    (1, 1.2345, 2.3456, 3.6),    
    (2, 1.2345, 2.3456, 3.58),   
    (3, 1.2345, 2.3456, 3.580),  
])
def test_precise_addition(precision, a, b, expected):
    calc = PreciseCalculator(precision=precision)
    assert calc.add(a, b) == expected
#-----------------------------------------------------------#

@pytest.mark.parametrize("precision, a, b, expected", [
    (0, 5.6789, 2.3456, 3.0),    
    (1, 5.6789, 2.3456, 3.3),    
    (2, 5.6789, 2.3456, 3.33),   
    (3, 5.6789, 2.3456, 3.333),  
])
def test_precise_subtraction(precision, a, b, expected):
    precise_calc = PreciseCalculator(precision=precision)
    assert precise_calc.subtract(a, b) == expected
#-----------------------------------------------------------#

@pytest.mark.parametrize("precision, a, b, expected", [
    (0, 1.2345, 2.3456, 3.0),    
    (1, 1.2345, 2.3456, 2.9),    
    (2, 1.2345, 2.3456, 2.9),    
    (3, 1.2345, 2.3456, 2.896),  
])
def test_precise_multiplication(precision, a, b, expected):
    precise_calc = PreciseCalculator(precision=precision)
    assert precise_calc.multiply(a, b) == expected
#-----------------------------------------------------------#

@pytest.mark.parametrize("precision, a, b, expected", [
    (0, 5.6789, 2.3456, 2.0),    
    (1, 5.6789, 2.3456, 2.4),    
    (2, 5.6789, 2.3456, 2.42),   
    (3, 5.6789, 2.3456, 2.421),  
])
def test_precise_division(precision, a, b, expected):
    precise_calc = PreciseCalculator(precision=precision)
    assert precise_calc.divide(a, b) == expected
#-----------------------------------------------------------#

@pytest.mark.parametrize("precision, a, b, expected", [
    (0, 2.3456, 2, 6.0),    
    (1, 2.3456, 2, 5.5),    
    (2, 2.3456, 2, 5.5),    
    (3, 2.3456, 2, 5.502),  
])
def test_precise_power(precision, a, b, expected):
    precise_calc = PreciseCalculator(precision=precision)
    assert precise_calc.power(a, b) == expected
#-----------------------------------------------------------#