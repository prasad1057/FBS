# 10. Write a program to reverse three-digit number.


number = int(input('Enter a three-digit number: '))

# Extract last digit
d1 = number % 10
number = number // 10

# Extract middle digit
d2 = number % 10
number = number // 10

# Extract first digit
d3 = number % 10

reverse_number = (d1 * 100) + (d2 * 10) + (d3 * 1)

print('Sum of three-digit number is:', reverse_number)