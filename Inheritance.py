class Parent():

    def print_last_name(self):
        print('Roberts')


# Inherits from Parent
class Child(Parent):

    def print_first_name(self):
        print('Bucky')

    # Overnight Parent
    '''
    def print_last_name(selfs):
        print('Bitan')
'''


bucky = Child()
bucky.print_first_name()
bucky.print_last_name()
