r, f = map(int, input().split())

# t is a variable for how many times the pan rotates 180 degrees
t = int(f/r)
remain = f%r

if t%2 == 0:
    if ((180/r)*remain < 270) and ((180/r)*remain > 90):
        print("down")
    else:
        print("up")
else:
    if ((180/r)*remain < 270) and ((180/r)*remain > 90):
        print("up")
    else:
        print("down")