a = 1 
b = 1
c = a + b 
numbers = [a,b,c]
while True:
    a = b
    b = c
    c = a + b
    numbers.append(str(c))
    if len(str(c)) >= 1000:
        print(len(numbers))
        break