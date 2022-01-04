# Each item in the list will be set to different variable
date, name, price = ['December 23, 2015', 'Guy Bitan', '8.51']
print(name)
print(date)
print(price)


def drop_first_last(grades):
    # Take the first item and list and save in the first var all the items in the middles and store in middle
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)


drop_first_last([65, 76, 98, 54, 21])
