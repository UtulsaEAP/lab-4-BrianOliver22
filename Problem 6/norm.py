"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Brian Oliver
Lab Time:
"""

def norm():
    # Write your code here
    list_num = int(input())
    my_list = []
    for i in range(list_num):
        numb = float(input())
        my_list.append(numb)
    highest_val = 0
    
    for i in range(list_num):
        if (highest_val < my_list[i]):
            highest_val = my_list[i]

    for i in range(list_num):
        my_list[i]= (my_list[i]/highest_val) 
        print(f'{my_list[i]:.2f}')

    

if __name__ == "__main__":
    norm()