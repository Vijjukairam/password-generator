import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    char_pool = ''
    
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_lowercase:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation
    
    if not char_pool:
        raise ValueError("At least one character set must be selected")
    
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

# Example usage
length = 16
password = generate_password(length)
print(f"Generated password: {password}")