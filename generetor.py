words=['python','CSS','HTML','JavaScript']

def word_edit_gen(word_list):
	for word in word_list:
		yield word.lower()

words_gen = word_edit_gen(words)

print(next(words_gen))
print(next(words_gen))