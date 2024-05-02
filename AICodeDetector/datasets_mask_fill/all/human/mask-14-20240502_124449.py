# Write <extra_id_0> that input a string <extra_id_1> user to delete a given <extra_id_2> a string.

text = <extra_id_3> string: ')
words = text.split()

data = input('Enter a word to delete: ')
status = False

for word in words:
    if word == data:
   <extra_id_4>    words.remove(word)
        status = <extra_id_5>    text = ' '.join(words)
    print('String after deletion:',text)
else:
    print('Word not present in string.')
