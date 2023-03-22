import re

specialChar = r'[!@#$%^&*()_+{}|:"<>?~\[\];\',./]'
alphanumeric = r'[A-Za-z0-9]'
capital_letter = r'[A-Z]'
errors = []

password = input("Please enter a new password containing at least 8 characters, \n"
                 "including at least one special character, one number, and one capital letter \n")
print(password)

# determine if password breaks any rules via regex
if len(password) < 8:
    errors.append("Password must contain at least 8 characters")
if not re.search(specialChar, password):
    errors.append("Password must contain at least one special character.")
if not re.search(alphanumeric, password):
    errors.append("Password must contain at least one number / letter.")
if not re.search(capital_letter, password):
    errors.append("Password must contain at least one capitalized letter\n")

# print any errors
if len(errors) == 0:
    print("Password is valid")
else:
    print("There was a problem with your password:\n")
    for error in errors:
        print(error)
