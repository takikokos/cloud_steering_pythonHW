def get_collatz_n(x):
    c = 0
    while x != 1:
        x = x // 2 if x % 2 == 0 else x * 3 + 1
        c += 1
    return c

print(get_collatz_n(int(input("Enter your number : "))))