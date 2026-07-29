from typing import Optional, Union, List, Dict, Tuple

def greet(name: str) -> str:
    return f"Hello, {name}"

def add(a: int, b: int) -> int:
    return a + b

def divide(a: float, b: float) -> Optional[float]:
    if b == 0:
        return None
    return a / b

def process(value: Union[int, str]) -> str:
    return str(value)

def total(numbers: List[int]) -> int:
    return sum(numbers)

def get_profile(user_id: int) -> Dict[str, Union[str, int]]:
    return {"id": user_id, "name": "Zeeshan", "age": 25}

def min_max(numbers: List[float]) -> Tuple[float, float]:
    return min(numbers), max(numbers)

print(greet("Zeeshan"))
print(add(3, 5))
print(divide(10, 3))
print(divide(10, 0))
print(process(42))
print(process("hello"))
print(total([1, 2, 3, 4, 5]))
print(get_profile(1))
print(min_max([3.5, 1.2, 8.9, 2.1]))
