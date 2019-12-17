def bin_polinomic(dec_str):
    bin_str = str(bin(int(dec_str)))[2:]
    mid = len(bin_str) + 1
    if bin_str[:mid] == bin_str[mid::-1]:
        return True
    else:
        return False


res = 0
# полиномы длины 6
for i in range(100, 1000):
    dec_str = str(i) + str(i)[::-1]
    if bin_polinomic(dec_str):
        res += int(dec_str)

# полиномы длины 4, 5
for i in range(10, 100):
    dec_str = str(i) + str(i)[::-1]
    if bin_polinomic(dec_str):
        res += int(dec_str) 

    # вставляем в середину    
    for j in range(10):
        dec_str = str(i) + str(j) + str(i)[::-1]
        if bin_polinomic(dec_str):
            res += int(dec_str)

# полиномы длины 2, 3
for i in range(1, 10):
    dec_str = str(i) + str(i)[::-1]
    if bin_polinomic(dec_str):
        res += int(dec_str)

    # вставляем в середину    
    for j in range(10):
        dec_str = str(i) + str(j) + str(i)[::-1]
        if bin_polinomic(dec_str):
            res += int(dec_str)

# полиномы длины 1
for i in range(1, 10):
    dec_str = str(i)
    if bin_polinomic(dec_str):
        res += int(dec_str)

print(res)
