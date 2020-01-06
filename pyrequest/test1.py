
def jump(n):
    if n == 0:
        return 0
    else:
        n -=1
        return 1+jump(n)

print(jump(2))
