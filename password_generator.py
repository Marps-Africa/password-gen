import string
import random
 
def generate_password(size):
   all_chars = string.ascii_letters + string.digits + string.punctuation
   password = ''
   for char in range(size):
       rand_char = random.choice(all_chars)
       password = password + rand_char
   return password
 
pass_len = int(input('How many characters in your password?'))
new_password = generate_password(pass_len)

with open('passwords_gen.txt', 'a') as f:
    f.write(new_password + '\n')
    
print('Here is Your new password: ', new_password)
