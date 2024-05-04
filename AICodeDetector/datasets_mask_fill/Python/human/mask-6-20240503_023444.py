print("Enter the String: ")
text = input()

print("Enter <extra_id_0> to Delete: ")
word = input()

text = text.replace(word, "")

print()
print(text)