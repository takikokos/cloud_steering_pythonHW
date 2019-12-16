data = input("Enter any data :\n")
while data != "":
    words = data.lower().split(" ")
    counter = {}

    for word in words:
        counter[word] = counter.get(word, 0) + 1
    maximum = max(counter.values())

    for word in counter:
        if counter[word] == maximum:
            print(f"{maximum} - {word}")

    data = input("\nEnter any data :\n")
