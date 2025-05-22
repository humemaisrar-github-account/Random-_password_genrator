#Random Password Genrator

# import random
# import string
# password_len =12
# char_val = string.ascii_letters + string.digits + string.punctuation
# password = "" 
# for i in range(password_len):
#     password += random.choice(char_val)

# print("your random  Password is :", password)    


#list comprehension[funtion for i in range(n)]
import random
import string
password_len =8
char_val = string.ascii_letters + string.digits + string.punctuation
 
password = "".join({random.choice (char_val) for i in range(password_len)})
print("your random Password is :", password) 

































