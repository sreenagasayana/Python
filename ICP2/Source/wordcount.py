file = open(r"/Users/jayantis/Documents/Python/Python.txt", "r")

content = file.read()
words = content.split("\n")
for i in words:
    print(i + "," + str(len(i)))

file.close()