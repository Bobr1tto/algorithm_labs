1. Реализация
```python
def multiplication_matrix(n):
    matrix = []

    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        matrix.append(row)

    return matrix
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

3. Реализация
```python
from time import perf_counter


def measure_time(func, data):
    start = perf_counter()
    func(data)
    end = perf_counter()
    return end - start

def multiplication_matrix(n):
    matrix = []

    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        matrix.append(row)

    return matrix

if __name__ == "__main__":
    sizes = [100, 1000, 5000, 10000]
    for n in sizes:
        t = measure_time(multiplication_matrix, n)
        print(n, t)
```
|         n          |            t           |
|--------------------|------------------------|
| 100                | 0.0041                 |
| 1000               | 0.1891                 |
| 5000               | 6.5074                 |
| 10000              | 28.8158                |