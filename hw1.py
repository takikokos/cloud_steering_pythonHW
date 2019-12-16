class NoLenNoBoolClass:
    def __init__(self):
        self.arr = [1, 2, 3]

    def __str__(self):
        return "NoLenNoBoolClass obj"

class ZeroLenClass:
    def __init__(self):
        self.arr = [1, 2 ,3]
        
    def __len__(self):
        return 0

    def __str__(self):
        return "ZeroLenClass obj"

class NotZeroLenClass:
    def __init__(self):
        self.arr = [1, 2, 3]

    def __len__(self):
        return 1

    def __str__(self):
        return "NotZeroLenClass obj"

class FalseBoolClass:
    def __init__(self):
        self.arr = [1, 2, 3]

    def __bool__(self):
        return False

    def __str__(self):
        return "FalseBoolClass obj"

testing_objects =  [0, 1, -1, 10, 
                    "", "1", "0", "qwerty", 
                    True, False, [], (), {}, 
                    [1, 2], (1, 2), {1:1, 2:2},
                    NoLenNoBoolClass(), ZeroLenClass(), NotZeroLenClass(),
                    FalseBoolClass(), None, 1.2, -3.4, 1+2j]

string_template = "{:^15}{:^25}{:^45}"

# bool интерпритирует 0 и None как False, все остальные обьекты int,
# complex и float как True, (класс bool на самом деле тоже int) 
# для всего остального вызывает метод __len__ или __bool__ и 
# интерпритирует то, что они вернули;
# если этих методов нет - возвращает True
print("\nПервое задание\n")
print(string_template.format("Bool val", "Object", "Class"))
print("-" * 85)
for obj in testing_objects:
    print(string_template.format(str(bool(obj)), str(obj), str(type(obj))))

# raw_input это ввести строку
# во втором питоне input() это то же самое что eval(raw_input()),
# это значит, что можно ввести сразу массив или вызвать функцию (как минимум),
# все что вы вводите выполняется интерпритатором питона;
# в третьем питоне input() это то же самое что и raw_input() во втором 
print("\nВторое задание\n")
def test():
    print("inside test func")
eval("test()")

# в третьем питоне print сделали функцией вместо ключевого слова,
# потому что это ключевое слово выделялось по смыслу то всех остальных,
# неудобно было перенаправлять вывод, тяжело было заменить какой либо другой функцией,
# не было возможности удобно управлять выводом (в третьем питоне можно использовать sep, end и т.д.)
print("\nТретье задание\n")
array_of_strings = ["first", "second", "third"]
print(*array_of_strings, sep=' line\n', end=' line\n')