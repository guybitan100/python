income = [10, 20, 30]


def double_money(dollars):
    return dollars * 2


# Get 'double_money' function and run it on 'income' list
new_income = list(map(double_money, income))

print(new_income)