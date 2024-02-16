"""
Complete the python code to find the solution to the system of linear equations entered by the user. 
The equations are of the form ax + by = c and dx + ey = f. The solution should be printed in the form x = # and y = #. 
If there is no solution, print "There is no solution".

Name: Brian Oliver
Lab Time: 2/16/2024 2:56
"""

def brute_eq():
    #Read in first equation, ax + by = c 
    a = int(input())
    b = int(input())
    c = int(input())

    #Read in second equation, dx + ey = f
    d = int(input())
    e = int(input())
    f = int(input())
    check = False
    for x in range(-10, 10, 1):
        for y in range(-10, 10, 1):
            if a * x + b * y == c and d * x + e * y == f:
               check = True
               print(x, y)
    else:
       if check == False:
               print('No solution')
    # YOUR CODE HERE
    
if __name__ == "__main__":
    brute_eq()