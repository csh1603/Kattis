n = int(input())

a = int(n/100)

if (n < 149):
    print(99)
elif (n%100 < 49) :
    print(a*100 - 1)
else:
    print((a+1)*100 - 1)