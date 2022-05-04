from fractions import Fraction

def fractionate(amount: int):
    return [Fraction(1, amount)] *amount

print(fractionate(5))