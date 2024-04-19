# Replace the "ANSWER HERE" for your answer
from math import sqrt

def roots(a, b, c):
    coefficient = b**2 - 4 * a * c
    
    if coefficient < 0:
        return "( )"
    
    root1 = (-b + sqrt(coefficient)) / 2
    root2 = (-b - sqrt(coefficient)) / 2

    if (root1 == root2): return f"({root1})"

    return f"({root1}, {root2})"


def value_y(a, b, c, x):
    return a * (x**2) + b * x + c


def to_string(a, b, c):
    response = "f(x) ="

    if a: response += f" {a} * X^2"
    if b: response += f"{' + ' if a else ' '}{b} * X"
    if c: response += f"{' + ' if a or b else ' '}{c}"

    return response

def derivation(a, b, _):
    response = f"f'(x) = "

    if not (a or b): return response + "0"
    
    if (a): response += f"{a * 2} * X"
    
    if (b): 
        response += f"{' + ' if a else ''}{b}"
    
    return response
