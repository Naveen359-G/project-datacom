import math

class ScientificCalculator:

    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        else:
            return num1 / num2

    def exponentiation(self, num1, num2):
        return num1 ** num2

    def root(self, num1, num2):
        if num1 < 0 and num2 % 2 == 0:
            return "Error: Negative number cannot have an even root"
        elif num1 < 0 and num2 % 2 != 0:
            return "Error: Negative number cannot have an odd root"
        else:
            return num1 ** (1.0 / num2)

    def logarithm(self, num1, base):
        if num1 <= 0:
            return "Error: Number must be greater than zero for logarithm"
        elif base <= 0:
            return "Error: Base must be greater than zero for logarithm"
        else:
            return math.log(num1, base)

    def sin(self, num):
        return math.sin(math.radians(num))

    def cos(self, num):
        return math.cos(math.radians(num))

    def tan(self, num):
        return math.tan(math.radians(num))

    def cosec(self, num):
        return 1 / math.sin(math.radians(num))

    def sec(self, num):
        return 1 / math.cos(math.radians(num))

    def cot(self, num):
        return 1 / math.tan(math.radians(num))

calc = ScientificCalculator()

print(calc.addition(10, 20))
print(calc.subtraction(30, 10))
print(calc.multiplication(5, 6))
print(calc.division(40, 5))
print(calc.exponentiation(3, 4))
print(calc.root(27, 3))
print(calc.logarithm(100, 10))
print(calc.sin(90))
print(calc.cos(0))
print(calc.tan(45))
print(calc.cosec(60))
print(calc.sec(30))
print(calc.cot(45))