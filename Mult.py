i_list = []
i_list.append(int(input()))

while True:
    a = int(input())

    if a % i_list[0] == 0:
        print(a)
        i_list = []

