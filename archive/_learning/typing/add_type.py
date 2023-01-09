# reasons to add typing
# add documentation
# linting
# auto complete

from typing import Dict, List, Set, Optional, Any, Sequence, Tuple, Callable, TypeVar

x: int = 1
print(x)


def add_number(a: int, b: int, c: int) -> int:
    return a + b + c


# b = add_number('a', 'b', 'c')
b = add_number(1, 1, 1)

print(b)


# starting with 3.9
# y: list[list[int]] = []


y: List[List[int]] = []


print(y)


z: Dict[str, str] = {"a": "b"}

bb: Set[str] = {'a', 'c'}


print(bb)


# custom type

Vector = List[float]
Vectors = List[Vector]


def foo(v: Vector) -> Vector:
    print(v)
    return v


foo([1.0, 3.9])


def foo2(v: Vectors) -> Vectors:
    return v


foo2([[3.9]])


def bar(seq: Sequence[str]):
    pass


bar(('1', '2', '3'))


c: Tuple[int, int, int] = (1, 2, 3)

# [int, int] inputs  int return type


def add(x: int, y: int) -> int:
    return x + y

# higher order function


def my_call(func: Callable[[int, int], int]) -> None:
    func(1, 2)


def my_call2() -> Callable[[int, int], int]:
    def add(x: int, y: int) -> int:
        return x + y
    return add


def my_lambda() -> Callable[[int, int], int]:
    func: Callable[[int, int], int] = lambda x, y: x + y
    return func


# Generic Type
# T is place holder
# has to be the same type
T = TypeVar('T')


def get_item(lst: List[T], index: int) -> T:
    return lst[index]


a = get_item([1, 2, 3, 4], 3)

print(a)
