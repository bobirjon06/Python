# text = "Hello world"
# wrd = text.split()
f = open("file.txt", "r")
text = f.read()
f.close()
wrd = text.split()
rslt = list()
for i in wrd:
    i = i[::-1]
    rslt.append(i)
print(rslt)
f = open("file1.txt", "w")
f.write(" ".join(rslt))
f.close()

f = open("file.txt", "r")
w = f.read()
f.close()
a = w.split("\n")
f1 = open("file2.txt", "w")
for i in a:
    f1.write(str(len(i))+"\n")

f1.close()