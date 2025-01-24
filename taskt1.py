#first_number  = input ()
#print(type(first_number))
#second_number  =input()
#print(type(second_number))

#result = first_number + second_number

#print(result)


#num1 = "4"
#any_var = "Mehwish"
#first_number = int(num1)
#print(type(first_number))
#num2 = "5"


# Task 1: Print "Hello, World!"
print("Hello, World!")

# Task 2: Concatenate first and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
print(f"Your full name is: {full_name}")

# Task 3: Simple Calculator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2
exponentiation = num1 ** num2
floor_division = num1 // num2

# Print results
print(f"The sum of {num1} and {num2} is {addition}.")
print(f"The difference when {num2} is subtracted from {num1} is {subtraction}.")
print(f"The product of {num1} and {num2} is {multiplication}.")
print(f"The division of {num1} by {num2} gives {division}.")
print(f"The modulus of {num1} and {num2} is {modulus}.")
print(f"The result of {num1} raised to the power of {num2} is {exponentiation}.")
print(f"The floor division of {num1} by {num2} gives {floor_division}.")

# Task 4: Draft email message
student_name = input("Enter the student's name: ")
roll_number = input("Enter the roll number: ")
class_venue = input("Enter the class venue: ")
class_schedule = input("Enter the class schedule: ")

# Using f-string
email_message_fstring = f"""
Dear {student_name},

Thank you for registering in the Python Programming course. Your roll number is {roll_number}. 
Your classes will be held in {class_venue} on {class_schedule}.

Best regards,
Python Programming Team
"""

# Using .format()
email_message_format = """
Dear {},

Thank you for registering in the Python Programming course. Your roll number is {}. 
Your classes will be held in {} on {}.

Best regards,
Python Programming Team
""".format(student_name, roll_number, class_venue, class_schedule)

# Print the email messages
print("\nEmail Message using f-string:")
print(email_message_fstring)

print("\nEmail Message using .format():")
print(email_message_format)
