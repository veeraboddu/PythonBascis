# square
for i in range(4):
    for j in range(4):
        print('# ',end="")

    print()

# staris
for i in range(4):
    for j in range(i+1):
        print("#",end="")
    print()
# reverse stairs
for i in range(4):
    for j in range(4-i):
        print("#",end="")
    print()