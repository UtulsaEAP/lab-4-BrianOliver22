"""
Complete the following python code to reverse the string entered by the user.

Name: Brian Oliver
Lab Time: 2/16 3
"""

def reverse_string():
    # YOUR CODE HERE
    my_list = []
    string = ""
    while (string != "done") and (string != "Done") and (string != "d"):
        my_list.append(string [::-1])
        string = str(input())
    
    sep = "\n"
    new_list = sep.join(my_list)
    print(new_list)
if __name__ == "__main__":
    reverse_string()