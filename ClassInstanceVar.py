class Girl:
    # Class Variable
    gender = 'female'

    # Instance Variable
    def __init__(self, name):
        self.name = name


r = Girl('Rachel')
s = Girl('Guy')

print(r.gender)
print(s.gender)
print(r.name)
print(s.name)
