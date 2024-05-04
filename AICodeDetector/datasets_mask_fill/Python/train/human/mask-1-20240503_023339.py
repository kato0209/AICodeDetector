# Write a <extra_id_0> input a string and ask
# user to delete a given word from a <extra_id_1> input('Enter a string: ')
words = text.split()

data = input('Enter a word to delete: ')
status = False

for word in <extra_id_2>   if word == data:
      <extra_id_3> words.remove(word)
        status = True

if status:
 <extra_id_4>  text = ' '.join(words)
    print('String after <extra_id_5>   print('Word not present in string.')
