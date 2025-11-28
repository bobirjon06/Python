#o'qish qiyin

#1

f2 = open("file.txt", 'r')

text = f2.read()
f2.close()

txt1 = text.split(".")

rmax = ""
for i in txt1:
    if len(i) > len(rmax):
        rmax = i
print(rmax)

#2
words = text.split()
count = 0
for i in words:
    i = i.strip(".,!?;:")
    if i == i[::-1]:
        count += 1
print(count)

#3

print(" ".join((sorted(words))))

#4

for i in words:
    for char in i:
        if char in "aeiou":
            break
    else:
        print(i)

#5

#yozish qiyin

#1

txt = "The lesson was long and tiring..."

f = open("file1.txt", 'w')
for i in txt:
    if i !=".":
        f.write(i)
f.close()

#2
f1 = open("palindrome.txt", 'w')
for i in words:
    i = i.strip(".,:;!?")
    if i == i[::-1]:
        f1.write(i+" ")
f1.close()

#3

# N = int(input())
N = 20
wrd = "again"
f = open("another.txt", 'w')
for i in range(N):
    f.write(wrd+" ")
f.close()

#4

f = open("another.txt", 'w')
for c in wrd:
    f.write(c+"\n")
f.close()

#5

f = open("another.txt", 'w')
for c in wrd:
    f.write(str(ord(c))+" ")
f.close()

#o'qish+yozish qiyin

#1

f1 = open("palindrome.txt", 'w')
for i in words:
    i = i.strip(".,:;!?")
    if i == i[::-1]:
        f1.write(i+" ")
f1.close()

#2

f = open("file.txt", 'r')
txt = f.read()
f.close()
words = txt.split()
words.sort(key=len)
# print(" ".join(words))
f1 = open("another.txt", 'w')
f1.write(" ".join(words))
f1.close()
#3

f = open("file.txt", 'r')
for line in f:
    count = 0
    for i in line:
        if i.isdigit():
            count += 1
    print(count, end=" ")
f.close()
# f = open("file.txt", 'r')

