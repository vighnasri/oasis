import random
import string

def generate_password(length):
    if length < 4:
        print("More than 4 characters are required for high Security")

    lowercase = string.ascii_lowercase  
    uppercase = string.ascii_uppercase  
    digits = string.digits              
    special_characters = string.punctuation  

    password = [ random.choice(lowercase), random.choice(uppercase), random.choice(digits), random.choice(special_characters) ]

   
    all_characters = lowercase + uppercase + digits + special_characters
    password += random.choices(all_characters, k=length - 4)

    random.shuffle(password)

    return ''.join(password)

def get_password_length():
    while True:
        length = int(input("enter your password required length:"))
        if length < 4:
            print("Length must be at least 4 characters!")
            continue
        return length

def main():
    
    length = get_password_length()
    
    password = generate_password(length)
        
    print("Your security password is:",password)
    print("Have Data Privacy with Secure Passwords")
    
if __name__ == "__main__":
    main()
