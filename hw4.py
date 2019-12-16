data = input("Enter any data :\n")
new_data = ""

for char in data:
    if char in "1234567890": # целые неотрицательные числа
        new_data += char
    else:
        new_data += " "

numbers = new_data.split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

print(sum(numbers))