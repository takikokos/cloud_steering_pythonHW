data = input("Enter any data :\n")
words = data.split(" ")
unique_words = set(words) # порядок слов будет другой

print("unique words :")
print(" ".join(unique_words))