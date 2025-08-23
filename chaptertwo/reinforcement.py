from collections.abc import Iterable
from typing import TypeAlias

# R_2.1

# 1. Spacecraft softwares 
# 2. X-ray machine softwares
# 3. Auto-pilot softwares

# R_2.2

# An operating system.

# R_2.3

# 

# R_2.4

class Flower:
    def __init__(self, name: str, petal_no: int, price: float):
        self._name = name
        self._petal_no = petal_no
        self._price = price

    def set_name(self, new_name: str):
        self._name = new_name
    
    def get_name(self):
        return self._name
    
    def set_petal_no(self, new_petal_no: int):
        self._petal_no = new_petal_no
    
    def get_petal_no(self):
        return self._petal_no
    
    def set_price(self, new_price: float):
        self._price = new_price

    def get_price(self):
        return self._price
    

# R_2.5

class CreditCard:

    def charge(self, price):
        if not isinstance(price, float | int): # make sure price is a number
            raise Exception("Price should be a number")

# R_2.6

class CreditCard:
    def make_payment(self, amount):
        if amount < 0:
            raise ValueError("Amount to deposit cannot be negative")
        

# R_2.7

class CreditCard:
    def __init__(self, customer, bank, acnt, limit, balance=0):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance

# R_2.8
    # wallet = []
    # for val in range(1, 60):
    #     wallet[0].charge(val)
    #     wallet[1].charge(2 * val)
    #     wallet[2].charge(3 * val)

    # changing the end of the range to 60, will cause the account balance of the third account
    # to go over its limit.


# R_2.9

# minuend and subtrahend
class Vector:

    def __sub__(self, subtrahend):
        if not isinstance(subtrahend, Vector):
            raise Exception('Can only perform vector subtraction with another vector')
        if len(subtrahend) != len(self):
            raise Exception('Can only subtract vectors of the same dimension.')
        new_coords = []
        for i in range(len(self)):
            new_coords.append(self._coords[i] - subtrahend._coords[i])
        result = Vector(len(new_coords))
        for i in range(len(new_coords)):
            result[i] == new_coords[i]
        return result
    

# R_2.10

def __neg__(self):
    result = Vector(len(self))
    for i in range(len(self)):
        result[i] == -1 * self[i]
    return result
    

# R_2.11

"""
The issue here is that when overloading opeartors, you have to define the behaviour for if that new data structure is used 
on the right hand side of the operation or if it is used on the left hand side of the operation.

In order for our datastructure to support the expression given in the question, we have to implement the __rmul__ method
for operator overloading.
"""

# R_2.12

def __mul__(self, value):
    dimension = len(self._coords)
    result = Vector(dimension)
    for i in range(self._coords):
        result[i] = self._coords[i] * value 
    return result   


# R_2.13

"""The solution for this is the same as 2.12, so instead of us writing the code again, what we 
can easily do is that we can assign __mul__ to __rmul__ that way we dont repeat ourself."""


# R_2.14

def __mul__(self, other):
    dimension = len(self._coords)
    if not isinstance(other, Vector):
        result = Vector(dimension)
        for i in range(dimension):
            result[i] = self._coords[i] * value
        return result
    if dimension != len(other):
        raise Exception('Cannot multiply vectors of different dimensions')
    scaler = 0
    for i in range(dimension):
        scaler += self._coords[i] + other[i]
    return scaler


# R_2.15

Number: TypeAlias = int | float

def __init__(self, dxi: Number | Iterable[Number]):
    if isinstance(dxi, Number):
        self._coords = [0] * dxi 
    else:
        self._coords = []
        for i in dxi:
            self._coords.append(i)


