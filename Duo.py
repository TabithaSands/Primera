import duolingo
lingo = duolingo.Duolingo('TabithaSan11', '##########')
my_known_words = lingo.get_known_words('hi')
for word in my_known_words:
    print(f'word {i} is: {word}')
    i = i+1
