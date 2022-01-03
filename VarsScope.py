# a is => Global variable available to all functions
a = 7823


def corn():
    b = 7824
    print(a)
    print(b)


def fudge():
    print(a)


corn()
fudge()
