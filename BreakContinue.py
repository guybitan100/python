'''
Break
'''

magicNum = 26

for n in range(101):
    if n == magicNum:
        print(n, " is the magic number")
        break
    else:
        print(n)

'''
Continue
'''

numbersTaken = [2, 5, 12, 33, 17]

for n in range(1, 20):
    if n in numbersTaken:
        continue
    print(n)

