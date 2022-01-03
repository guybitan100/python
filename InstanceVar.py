class Girls:
    # Class Variable like static
    gender = 'female'

    def __init__(self, name):
        # Instance Variable
        self.name = name


r = Girls('guy1')
s = Girls('guy2')
print(r.gender)
print(s.gender)
print(r.name)
print(s.name)
