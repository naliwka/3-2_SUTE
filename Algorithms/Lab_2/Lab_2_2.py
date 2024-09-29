text = input("Enter a text:")
words = text.lower().split()

dict = {}
for word in words:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

sorted_dict = sorted(dict.items(), key=lambda item: item[1])

print("Dictionary:", dict)
if len(sorted_dict) >= 3:
    i = 3
else:
    i = len(sorted_dict)

print("Most common words:")
for word, count in sorted_dict[-i:]:
    print(word)


