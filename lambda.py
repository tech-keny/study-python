words =['Python','CSS','HTML','JavaScript']

def word_edit(word_list,func):
	new_words=[]
	for word in word_list:
		new_word = func(word)
		new_words.append(new_word)

	return new_words

print(word_edit(words, lambda word:word.lower()))

print(word_edit(words, lambda word:word.upper()))