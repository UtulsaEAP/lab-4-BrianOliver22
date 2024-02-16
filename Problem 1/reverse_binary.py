"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Brian Oliver
Lab Time:

"""


def reverse_binary():
    user_num = int(input())
    # YOUR CODE HERE


    bin_num = bin(user_num)
    great = bin_num.lstrip('0b',)
    better = bin_num.lstrip('-0b')
    good = better [::-1]
    print(good)
          
if __name__ == "__main__":
    reverse_binary()