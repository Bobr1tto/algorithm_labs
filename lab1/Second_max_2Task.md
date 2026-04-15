1. Реализация
```python
def second_max(arr):
    max1 = arr[0]
    max2 = arr[0]
    for i in arr:
        if i > max1:
            max2 = max1
            max1 = i
    return max2
```

2. Функция измерения времени
```python
from time import perf_counter


def measure_time(func, data):
    start = perf_counter()
    func(data)
    end = perf_counter()
    return end - start
```

3. Функция генерации данных
```python 
from random import randint


def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(randint(0, 10_000))
    return arr
```

4. Эксперимент
```python
from time import perf_counter
from random import randint


def second_max(arr):
    max1 = arr[0]
    max2 = arr[0]
    for i in arr:
        if i > max1:
            max2 = max1
            max1 = i
    return max2


def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(randint(0, 10_000))
    return arr


def measure_time(func, data):
    start = perf_counter()
    func(data)
    end = perf_counter()
    return end - start


if __name__ == "__main__":
    sizes = [100, 1000, 5000, 10000]
    for n in sizes:
        arr = generate_array(n)
        t = measure_time(second_max, arr)
        print(n, t)
```

|         n          |            t           |
|--------------------|------------------------|
| 100                | 0.00003689998993650079 |
| 1000               | 0.00014399999054148793 |
| 5000               | 0.0003564999788068235  |
| 10000              | 0.0006273000035434961  |
