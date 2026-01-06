"""Calculator module."""

from utils import add, subtract, multiply

class Calculator:
    def calculate(self, op, a, b):
        if op == '+':
            return add(a, b)
        elif op == '-':
            return subtract(a, b)
        elif op == '*':
            return multiply(a, b)
        else:
            raise ValueError(f"Unknown operation: {op}")
