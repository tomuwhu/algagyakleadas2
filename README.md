# Algoritmusok és adatszerkezetek gyakorlati feladatok

## Dr. Németh Tamás

- aa sd fesf
- s dfdsf d

[link](https://tomuwhu.github.io/algagyakleadas2/f1.py)

```python
def h(n, a, b, c):
    if n == 1:
        yield f"{a} => {c}"
    else:
        yield from h(n - 1, a, c, b)
        yield f"{a} => {c}"
        yield from h(n - 1, b, a, c)
n = int(input())
print(2 ** n - 1)
print(*h(n, 1, 2, 3), sep = "\n")
```

$f(n, a, b, c) =$

    ha n = 1:
$$a⇒c$$

    különben:
$$ f(n - 1, a, c, b), a ⇒ c + f(n - 1, b, a, c)$$
