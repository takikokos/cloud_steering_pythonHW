numbers = input("Enter numbers : \n").split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
numbers.sort()

ans = numbers[0]
if ans == 1:
    for i in range(len(numbers)):
        if i == (len(numbers) - 1) or numbers[i]+1 < numbers[i+1]:
            ans = numbers[i]+1
            break
else:
    ans = 1
print(ans)


# с set
all_possible_answers = set(range(1, max(numbers) + 2))
all_possible_answers = all_possible_answers - set(numbers)
print(min(all_possible_answers))