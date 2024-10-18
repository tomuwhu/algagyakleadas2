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