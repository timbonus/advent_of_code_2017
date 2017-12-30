with open('04_input.txt','r') as f:
    x = f.read()

phrases = x.split('\n')
valid_count = 0

for phrase in phrases:
    words = phrase.split()
    good = True
    if len(phrase) > 1:
        words.sort()
        for loc,word in enumerate(words):
            if (loc > 0) and (word == words[loc-1]):
                good = False
        valid_count += good

print(len(phrases))
print(valid_count)
