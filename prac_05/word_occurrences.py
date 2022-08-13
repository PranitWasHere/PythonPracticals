count_words = {}
user_text = input("Text: ")
words = user_text.split()
for word in words:
    frequency = count_words.get(word, 0)
    count_words[word] = frequency + 1

words = list(count_words.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, count_words[word]))