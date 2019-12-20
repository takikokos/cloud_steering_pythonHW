def letters_range(start : str, stop : str, step : int = 1) -> list:
    assert len(start) == len(stop) == 1
    return [chr(x) for x in range(ord(start), ord(stop), step)]


print("test #1 : ", letters_range('b', 'w', 2) == ['b', 'd', 'f', 'h', 'j', 'l', 'n', 'p', 'r', 't', 'v'])

print("test #2 : ", letters_range('a', 'g') == ['a', 'b', 'c', 'd', 'e', 'f'])

print("test #3 : ", letters_range('g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'])

print("test #4 : ", letters_range('p', 'g', -2) == ['p', 'n', 'l', 'j', 'h'])

print("test #5 : ", letters_range('a','a') == [])
