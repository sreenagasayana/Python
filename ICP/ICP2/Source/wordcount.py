file = open(r"/Users/jayantis/Documents/Python/Python.txt", "r")

content = file.read()
words = content.split("\n")
f = open('/Users/jayantis/Documents/Python/output.txt','w')
for i in words:
    f.write(i + "," + str(len(i)))
    f.write("\r")

f.close()

file.close()