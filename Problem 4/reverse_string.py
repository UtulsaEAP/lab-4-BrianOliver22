"""
Complete the following python code to reverse the string entered by the user.

Name: Brian Oliver
Lab Time:
"""

def reverse_string():
    # YOUR CODE HERE
    my_list = [" "]
    string = "fun"
    while (string != "done" or string != "d" or  string != "Done") :
        string = str(input())
        my_list.append(string [::-1])
    """""
    new = " "
    s1= ""
    for c in s:
        s1
    s.append()
"""
    sep = "\n"
    new_list = sep.join(my_list)
    print(new_list)
if __name__ == "__main__":
    reverse_string()