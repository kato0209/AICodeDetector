print("Enter the String: ")
text = input()

print("Enter the Word to Delete: ")
word = input()

text = text.replace(word, "")

print()
print(text)