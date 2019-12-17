def bin_palindromic(dec_str):
    bin_str = format(int(dec_str), "b")
    return bin_str == bin_str[::-1]

def sum_palindroms(pali_length):
    '''
        Возвращает сумму всех палиндромов заданной длины в 
        10ом представлении числа, которые также являются 
        палиндромами в двоичном представлении

        Палиндром симетричен относительно своей середины,
        для числа n будут перебираться (10^ceil(lg(n) / 2))
        десятичных чисел, отражая которые получатся все возможные 
        палиндромы заданной длины

        pali_length : int
    '''
    # тривиальный случай, вернуть сумму чисел от 1 до 9 которые 
    # являются палиндромами в бинарном представлении 
    if pali_length == 1:
        return sum([x for x in range(1, 10) if bin_palindromic(str(x))])

    # insert_mid : bool - нужно ли вставлять цифру в середину,
    # нужно для палиндромов нечетной длины
    insert_mid = pali_length % 2 == 1

    # степень десятки, показывает сколько разрядов занимает половина палиндрома
    pow = (pali_length - 1) // 2 if insert_mid else pali_length // 2
    res = 0
    if insert_mid:
        for i in range(10**(pow-1), 10**pow):
            for j in range(10):
                dec_str = str(i) + str(j) + str(i)[::-1]
                if bin_palindromic(dec_str):
                    res += int(dec_str)
    else:
        for i in range(10**(pow-1), 10**pow):
            dec_str = str(i) + str(i)[::-1]
            if bin_palindromic(dec_str):
                res += int(dec_str)
    return res


res = 0

for i in range(1, 7):
    res += sum_palindroms(i)

print(res)
