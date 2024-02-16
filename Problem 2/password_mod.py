"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name: Brian Oliver
Lab Time: 2/16/2024
"""

def password_mod():
    word = input()
    password = ''
    # Type your code here.
    #txt = str(input())
    password= word.replace("i","1")
    password= password.replace("a","@")
    password= password.replace("m","M")
    password = password.replace("B","8")
    password= password.replace("s","$")


if __name__ == "__main__":
    password_mod()