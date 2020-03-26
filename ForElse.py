
# for else condition if does not exist in for loop print else statement
num = [11,12,13,14,16]

for i in num:
    if i % 5 == 0:
        print(num)
        break
else:
    print("Not found")