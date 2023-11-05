my_name = "Anar"
# Taking input from user
user_name = input("What is your name: ")

print(f"Hello, {user_name}! My name is {my_name}")

user_age = input("How old are you? ")



# The input from user is taken as a string
# If we want to convert it to integer we need to use int() function
print(f"{user_name} is {user_age} years old")
# print(f"{user_name} has lived {int(user_age) *12} months")

# or we can do this way
# user_age = int(input("How old are you? "))

months = int(user_age)*12
print(f"{user_name} has lived {months} months")


 # BOOLEANS

my_age = 22
user_age = int(input("How old are you? "))

# The values of the following 3 variables are either TRUE or FALSE
# Bases on the user input
checking = my_age == user_age
checking_older = my_age >user_age
checking_younger = my_age <user_age


print(f"Our ages match: {checking}")
print(f"I am older: {checking_older}")
print(f"I am younger: {checking_younger}")


# and & or
user_age = int(input("Your age: "))

valid_age_and = user_age>18 and user_age <35
print(f"Your age is valid for military: {valid_age_and}")

valid_age_or = user_age <16 or user_age >65
print(f"You can get discount: {valid_age_or}")




bool(0) #This is false
bool(73) #This is true


bool("") #This is false
bool("This is true") #This is true

bool([]) #This is false
bool([10, 737]) #This is true



# In this example, if user enters name then in the last print statement
# The entered name will be printed
# If user does not enter a name
# Then default_name value will be printed
default_name = "User"
user_name = input("What is your name:(optioanl) ")

name_of_user = user_name or default_name
print(f"Hello, {name_of_user}")


age = 16
side_job = True
print(age > 18 and age < 65 or side_job)
# The output of this will be True, because:
# First it checks the comparisons(>, <) from left to right
# Which gives us false and true or true
# then it starts checking from left to right 
#false and true gives us false
# then false or side_job will be checked
# as value of side_job is true, we get false or True
# and it will give us true