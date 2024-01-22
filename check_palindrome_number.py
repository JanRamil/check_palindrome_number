# Check Palindrome Number
# Exercise 9

# Create a pseudocode

# Create a code that will input your desired number
input_number = int(input("Please enter your desired number: "))

# Create a code that will print the number you entered
print("The original number is", input_number)

# reverse the given number
number = input_number
rev_number = 0
while number > 0:
    remainder = number % 10
    rev_number = (rev_number * 10) + remainder
    number = number // 10

