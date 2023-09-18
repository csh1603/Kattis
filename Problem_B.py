ann = input()
ben = input()

ann_list = []
for letter in ann:
    ann_list.append(letter)

ben_list = []
for letter in ben:
    ben_list.append(letter)

len = max(len(ann), len(ben))

a = 0
b = 0
final = []

for i in range(len):
    if (ann_list[a] <= ben_list[b]):
        final.append(ann_list[a])
        a += 1
    else:
        final.append(ben_list[b])
        b += 1

if (a > i):
    while (len(ann_list) == a):
        final.append(ann_list[a])
        a += 1
elif (b > i):
    while (len(ben_list) == b):
        final.append(ben_list[b])
        b += 1

print(str(final))