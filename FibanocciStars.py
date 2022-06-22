def starPrint(n):
    while n > 0:
        print('* ',end=' ')
        n -= 1


def spacePrint(n):
    while n > 0:
        print(' ', end=' ')
        n -= 1


N = int(input('enter required number of fibanocci steps- '))
star = 1
space = N - 1
itert = 0
while space >= 0:
    spacePrint(space)
    space -= 1
    while star + space < N:
        starPrint(star)
        print()
        star += 1
