"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name: Brian Oliver
Lab Time: 2/16/2024
"""

def password_mod():
    word = str(input())
    password = ''
    for letter in word:
        if letter == "i" : 
            letter = "1"
        elif letter == "a" :
            letter = "@"
        elif letter == "m":
            letter = "M"
        elif letter == "B":
            letter = "8"
        elif letter == "s":
            letter = "$"
        password = password + letter
    
    password = password+"!"

    print(password)
    # Type your code here.
    #txt = str(input())

if __name__ == "__main__":
    password_mod()