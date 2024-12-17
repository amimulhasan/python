# -*- coding: utf-8 -*-
"""check_email_validation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1a0zHxDV2NyAZStfT4llrvKnZih7EFnkV
"""

import re
email_condition='^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w {2,3}$'



user_email=input('enter your email: ')
if re.search(email_condition,user_email):
  print('Right email')
else:
  print('Wrong email')

import re

def validate_email(email):
    # Define a regex pattern for validating email
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Match the pattern with the input email
    if re.match(email_pattern, email):
        return True
    else:
        return False

# Example usage
email = input("Enter an email address to validate: ")
if validate_email(email):
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is not a valid email address.")

import re

def validate_email(email):
    # Regex pattern: email must start with a letter (a-z or A-Z)
    email_pattern = r'^[a-zA-Z][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Match the pattern with the input email
    if re.match(email_pattern, email):
        return True
    else:
        return False

# Example usage
email = input("Enter an email address to validate: ")
if validate_email(email):
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is not a valid email address.")

import re
def validation_email(email):
  email_pattern=r'^[a-zA-Z][a-zA-z0_9._%+-]*@[a-zA-Z0-9.-]+[a-zA-z]{2,}$'
  if re.match(email_pattern,email):
    return True
  else:
    return False
email=input('enter your mail:')
if validation_email(email):
  print(f'{email} is a valid')
else:
  print(f'{email} is not a valid')