x = int(input())
i = 0
while x > 1:
    if x % 2 == 0:
        x=x/2
        i += 1
    elif x % 2 == 1:
        i += 1
        x = x+1

print(i)