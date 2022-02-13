## project euler 2. question's solve
a = 1
b = 2
c = a + b
total = 2
while c < 4000000:
    a = b
    b = c 
    c = a + b
    if c % 2 == 0:
        total += c
print(total)