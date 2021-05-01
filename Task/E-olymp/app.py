

''' x = int(input())

print(x//1000, (x//10) % 10, x % 10, sep="")


x = int(input())

if x < -4:
    print(x+5)
elif -4 <= x and x <= 7:
    print(x**2 - 3*x)
elif x > 7:
    print(x**3 + 2*x)
 '''

''' x = int(input())

print(x//10,x//10,x%10,x%10, sep='') '''


''' a = list(input().split())


print(min(a))




 '''


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
