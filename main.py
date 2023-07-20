def natural(a):
    if a == 1:
        print(1)
        return 1
    natural(a - 1)
    print(a)
a = int(input())
natural(a)
