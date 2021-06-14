word_count = {}
with open('poem.txt', 'r') as handle:
    for line in handle:
        print(line)
        words = line.split(' ')
        for word in words:
            word = word.replace('\n', '')
            word_count[word] = word_count.get(word, 0) + 1

print(word_count)
