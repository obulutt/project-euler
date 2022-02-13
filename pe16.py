## project euler 16. question
numbers = []
total = 0
a = 2 ** 1000
a = str(a)
for i in a:
    numbers.append(i)
for i in numbers:
    i = int(i)
    total += i
print(total)