def bin_polinomic(dec_str):
    bin_str = str(bin(int(dec_str)))[2:]
    mid = len(bin_str) + 1
    if bin_str[:mid] == bin_str[mid::-1]:
        return True
    else:
        return False

def sum_polynoms(poly_length):
    if poly_length == 1:
        return sum([x for x in range(1, 10) if bin_polinomic(str(x))])
    insert_mid = poly_length % 2 == 1
    pow = int((poly_length - 1) / 2) if insert_mid else int(poly_length / 2)
    res = 0
    if insert_mid:
        for i in range(int(10**(pow-1)), int(10**pow)):
            for j in range(10):
                dec_str = str(i) + str(j) + str(i)[::-1]
                if bin_polinomic(dec_str):
                    res += int(dec_str)
    else:
        for i in range(int(10**(pow-1)), int(10**pow)):
            dec_str = str(i) + str(i)[::-1]
            if bin_polinomic(dec_str):
                res += int(dec_str)
    return res


res = 0

for i in range(1, 7):
    res += sum_polynoms(i)
    
print(res)
