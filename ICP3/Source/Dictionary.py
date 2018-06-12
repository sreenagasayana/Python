word = input("enter your sentence:-")

wordslist = word.split(" ")

wordslist.sort()

#print(wordslist)

frequency = {}
count = 0
for w in wordslist:
    frequency[w] = wordslist.count(w)
print(frequency)