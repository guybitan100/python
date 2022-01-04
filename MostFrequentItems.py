from collections import Counter

test = " we hope to one one day become the world's leader in free"

words = test.split()

counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)