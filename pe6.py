sum_of_squares = 0
square_of_the_sum = 0
sum = 0

for i in range(101):
    sum += i
    sum_of_squares += i**2
square_of_the_sum = sum **2

result = square_of_the_sum - sum_of_squares
print(result)
