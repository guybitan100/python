from operator import itemgetter

users = [
    {'FirstName': 'Bucky', 'LastName': 'Roberts'},
    {'FirstName': 'Tom', 'LastName': 'Roberts'},
    {'FirstName': 'Bernie', 'LastName': 'Zunks'},
    {'FirstName': 'Jenna', 'LastName': 'Hayes'},
    {'FirstName': 'Sally', 'LastName': 'Jones'},
    {'FirstName': 'Amanda', 'LastName': 'Roberts'},
    {'FirstName': 'Tom', 'LastName': 'Williams'},
    {'FirstName': 'Dean', 'LastName': 'Hayes'},
    {'FirstName': 'Bernie', 'LastName': 'Barbie'},
    {'FirstName': 'Tom', 'LastName': 'Jones'}
]

for x in sorted(users, key=itemgetter('FirstName')):
    print(x)

print('----------')
for x in sorted(users, key=itemgetter('FirstName', 'LastName')):
    print(x)
