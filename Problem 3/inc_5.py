"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name: Brian Oliver
Lab Time:
"""

def inc_5():
    # Write your code here
    print("put integer 1 here")
    int1= int(input())
    print("put integer 2 here")
    int2 = int(input())
    int3 = int1
    int4 = str(int1)
    #s=" "
    my_list = [str(int4)]
    while (int1 < int2):
        int1 += 5
        my_list.append(str(int1))
    #combined = s.join(combined)
    if (int3>int2):
        my_list = "Second integer can't be less than the first."
    
    generator_expr = (str(element) for element in my_list)
    separator = ", "
    result_string = separator.join(generator_expr)
    print(result_string)

if __name__ == '__main__':
    inc_5()
