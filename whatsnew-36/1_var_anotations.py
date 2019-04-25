from typing import Iterable, List

x: List[float] = []
x.extend([1, 2, 3])

y: List[int] = []
y.extend([4., 5., 6.])  # only upsets ide

print(f'module annotations {__annotations__}')


def dot_product(x: Iterable[float], y: Iterable[float]) -> float:
    return sum(xi*yi for xi, yi in zip(x, y))


print(dot_product.__annotations__)


result = dot_product(x, y)
print(f'result: {result}')
