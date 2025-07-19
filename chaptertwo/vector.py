from __future__ import annotations
from typing import List, TypeAlias
from decimal import Decimal

Number: TypeAlias = int | float | Decimal
VectorComponents : TypeAlias = List[Number]


class Vector:
    def __init__(self, components: VectorComponents) -> None:
        self._components = components
    def get_components(self):
        return self._components
    def __add__(self, summand: Vector) -> Vector:
        summand_components: VectorComponents = summand.get_components()
        if len(self._components) != len(summand_components):
            raise ValueError('Error: Cannot add two vectors of different dimensions')
        newComponent = [a + b for a, b in zip(self._components, summand_components)] # type: ignore
        return Vector(newComponent)
    def __repr__(self) -> str:
        return f'Vector({self._components})'

a = Vector([1,2,3])
b = Vector([4,5,6])
c = b + a
print(c.get_components())
print(c)