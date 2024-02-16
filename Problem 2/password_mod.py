"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name: Brian Oliver
Lab Time: 2/16/2024
"""

def password_mod():
    word = input()
    password = ''
    # Type your code here.
    txt = str(input())
    x= txt.replace("i","1")
    x= x.replace("a","@")
    x= x.replace("m","M")
    x = x.replace("B","8")
    x= x.replace("s","$")
    print(x)

if __name__ == "__main__":
    password_mod()