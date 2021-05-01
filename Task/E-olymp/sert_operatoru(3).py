x = int(input())

if x < -4:
    print(x+5)
elif -4 <= x and x <= 7:
    print(x**2 - 3*x)
elif x > 7:
    print(x**3 + 2*x)