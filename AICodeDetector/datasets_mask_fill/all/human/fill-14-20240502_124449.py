# Write a method that input a string and then ask the user to delete a given word from a string.

text = input('Enter a string: ')
words = text.split()

data = input('Enter a word to delete: ')
status = False

for word in words:
    if word == data:
   #    words.remove(word)
        status = True    text = ' '.join(words)
    print('String after deletion:',text)
else:
    print('Word not present in string.')
