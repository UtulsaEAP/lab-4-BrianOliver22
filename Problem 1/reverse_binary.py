"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Brian Oliver
Lab Time:

"""


def reverse_binary():
    user_num = int(input())
    # YOUR CODE HERE
    lst = []
    new = user_num
    while (user_num > 0.99999):
        new = (user_num % 2)
        lst.append(str(new))
        user_num = int(user_num/2)
    lst = lst [::1]
    sep = "\n"
    lst = sep.join(lst)
    print(lst)
"""""
    bin_num = bin(user_num)
    great = bin_num.lstrip('0b',)
    better = bin_num.lstrip('-0b')
    good = better [::-1]
    print(good)
        """
if __name__ == "__main__":
    reverse_binary()