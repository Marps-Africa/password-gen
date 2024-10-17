# Random Password Generator script

This Python program generates a random password of a specified length.

## Usage

1. Run the script.
2. Enter the desired password length.

## Features
* Generates strong passwords with a mix of letters, numbers, and symbols.
* Saves generated passwords to a file for easy reference.

## Code Explanation

```python
import string
import random

def generate_password(size):
    # Combine all possible characters
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Initialize an empty password string
    password = ''

    # Generate random characters and append them to the password
    for char in range(size):
        rand_char = random.choice(all_chars)
        password = password + rand_char

    return password

# Get the desired password length from the user
pass_len = int(input('How many characters in your password?'))

# Generate the new password
new_password = generate_password(pass_len)

# Append the new password to a file
with open('passwords_gen.txt', 'a') as f:
    f.write(new_password + '\n')

# Print the generated password
print('Here is Your new password: ', new_password)
```
## Execution
1. Open a Terminal
2. Navigate to the directory you saved the script
3. Run the script using this command, `python password_generator.py`
