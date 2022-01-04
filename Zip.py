first = ['Guy', 'Tom', 'Taylor']
last = ['Bitan', 'Nativ', 'Golan']
phone = ['00001', '00002', '00003']
# The results is map
names = zip(first, last, phone)
# Results
# [('Guy','Bitan'),('Tom','Nativ'),('Taylor','Golan')]

for a, b, c in names:
    print(a, b, c)
