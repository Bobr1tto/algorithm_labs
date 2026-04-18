1. Реализация
```python
def Binary_search(arr, search_value):
    right = len(arr) - 1
    left = 0

    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == search_value:
            return "Target is found"
        elif arr[mid] < search_value:
            left = mid + 1
        else:
            right = mid - 1
    return "Target is NOT found"
```

2. Функция измерения времени
```python
from time import perf_counter

def measure_time(func, *data):
    start = perf_counter()
    func(*data)
    end = perf_counter()
    return end - start
```

3. Функция генерации данных
```python
def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(randint(0, 10_000))
    arr.sort()
    return arr
```

4. Реализация
```python
from time import perf_counter
from random import randint


def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(randint(0, 10_000))
    arr.sort()
    return arr

def measure_time(func, *data):  #плохо работает при слишком бысрых скоростях, погрешность перекрывает
    start = perf_counter()
    func(*data)
    end = perf_counter()
    return end - start

def Binary_search(arr, search_value):
    right = len(arr) - 1
    left = 0

    while left <= right:
        mid = (right + left) // 2
        if arr[mid] == search_value:
            return "Target is found"
        elif arr[mid] < search_value:
            left = mid + 1
        else:
            right = mid - 1
    return "Target is NOT found"

if __name__ == "__main__":
    sizes = [100, 1000, 5000, 10000]
    for n in sizes:
        arr = generate_array(n)
        t = measure_time(Binary_search, arr, randint(0, 10_000))
        print(n, t)
```
|         n          |            t           |
|--------------------|------------------------|
| 100                |  0.0000002             |
| 1000               |  0.0000002             |
| 5000               |  0.0000002             |
| 10000              |  0.0000002             |

