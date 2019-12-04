def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    if(a == 0 and b == 0):
        if(c == 0):
            print(0)
        else:
            raise ValueError("równanie sprzeczne")
    elif(a == 0):
        print(-b/c)
    elif(b == 0):
        print(-c/a)
    else:
        print("{0}+({1} * x)".format(-c/b, -a/b))


solve1(1, 2, 3)