from functools import reduce


def problem6():
    return sum(range(1, 101))**2 - sum([x**2 for x in range(1, 101)])

def problem9():
    return [a * b * c for a in range(1, 1001) for b in range(a, 1001) for c in range(b, 1001) if a + b + c == 1000 and a**2 + b**2 == c**2][0]

def problem48():
    return str(sum((x**x for x in range(1, 1001))))[-10:]

def problem40():
    return reduce(lambda x, y: x*y, [ int("".join((str(x) for x in range(1, 10**6)))[10**i-1]) for i in range(7) ], 1)
    

print("problem6 = ", problem6())
print("problem9 = ", problem9())
print("problem48 = ", problem48())
print("problem40 = ", problem40())