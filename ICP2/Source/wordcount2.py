f = open(r"/Users/jayantis/Documents/Python/Python2.txt", "r")

content = f.read()
line = content.split("\n")

for n in line:
    word = n.split(" ")
    print( " ".join(word), len(word))
f.close()