def fib(n):
    ''' Вычисляет n-ый эл-т последовательности Фиббоначи '''
    cur, next = 1, 1
    for i in range(n):
        cur, next = next, cur+next
    return cur

for i in range(10):
    print(f"{i} элемент - {fib(i)}")