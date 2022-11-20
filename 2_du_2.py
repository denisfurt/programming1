sevenCharWords = []

newWord = ''

while newWord != "-1":
    newWord = input();

    if len(newWord) > 10:
        sevenCharWords.append(newWord);

for i in sevenCharWords:
    print(i)
