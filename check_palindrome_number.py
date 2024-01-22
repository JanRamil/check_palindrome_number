# Check Palindrome Number
# Exercise 9

# Create a pseudocode

# Create a code that will input your desired number
input_number = int(input("Please enter your desired number: "))

# Create a code that will print the number you entered
print("The original number is", input_number)

# Create a code that reverse the given number
number = input_number
rev_number = 0
while number > 0:
    remainder = number % 10
    rev_number = (rev_number * 10) + remainder
    number = number // 10

# Create a code that will check if the given number is equal to the reversed number
if input_number == rev_number:
    # if yes, print True message
    print("Yeyyy, The given number is a palindrome number.")
else:
    # else, print False message
    print("Oh no, The given number is not a palindrome number.")