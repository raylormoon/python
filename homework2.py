
# Name: Tianjiao Xu

# Instructions:
#  In this assignment, we will practice writing control flow for loops.

# Problem 1.

def square_root_for(a, x0, max_iter = 10, tol=1e-14):
    """ (number, integer, number) -> float

    Return an estimate of the square root of a number using the Heron's method.
        
    >>> square_root_for(5, 5)
    Iteration | Estimate         | Relative Change
    -------------------------------------------------
    1         | 3.00000000000000 | 0.4000000000000000
    2         | 2.33333333333333 | 0.2222222222222222
    3         | 2.23809523809524 | 0.0408163265306123
    4         | 2.23606889564336 | 0.0009053870529653
    5         | 2.23606797749998 | 0.0000004106060359
    6         | 2.23606797749979 | 0.0000000000000842
    7         | 2.23606797749979 | 0.0000000000000000
    2.23606797749979
    """
    print('Iteration | Estimate         | Relative Change')
    print('-------------------------------------------------')
    x0=5
    x1=x0
    for i in range(1,max_iter):
        xk1 =1/2 * (x1+a/x1)
        relative_error=abs(xk1-x1)/x1
        print("{0:<9} | {1:.14f} | {2:.16f}".format(i,xk1,relative_error))
        if (relative_error < tol):
            break
        x1=xk1
    return  xk1
    
           
# Don't change or delete the 5 lines of code below.
a = 5
max_iter = 100
tol = 1e-15
x_final = square_root_for(a, a, max_iter, tol)
print('Final estimate using square_root_for is {0}'.format(x_final))


#problem 2

def square_root_while(a, x0, tol=1e-14):
    """ (number, number, number) -> float

    Return an estimate of the square root of a number using the Heron's method.
        
    >>> square_root_while(5, 5)
    Iteration | Estimate         | Relative Change
    -------------------------------------------------
    1         | 3.00000000000000 | 0.4000000000000000
    2         | 2.33333333333333 | 0.2222222222222222
    3         | 2.23809523809524 | 0.0408163265306123
    4         | 2.23606889564336 | 0.0009053870529653
    5         | 2.23606797749998 | 0.0000004106060359
    6         | 2.23606797749979 | 0.0000000000000842
    7         | 2.23606797749979 | 0.0000000000000000
    2.23606797749979
    """
    print('Iteration | Estimate         | Relative Change')
    print('-------------------------------------------------')
    x0=5
    i=1
    x1=x0
    relative_error=float("inf")
    while i<max_iter:
        xk1 =1/2 * (x1+a/x1)
        relative_error=abs(xk1-x1)/x1
        print("{0:<9} | {1:.14f} | {2:.16f}".format(i,xk1,relative_error))
        if relative_error<tol:
            break
        x1=xk1
        i+=1
    return xk1
        
# Don't change or delete the 4 lines of code below.
a = 5
tol = 1e-15
x_final = square_root_while(a, a, tol)
print('Final estimate using square_root_while is {0}'.format(x_final))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print('Final estimate using square_root_for is {0}'.format(x_final))
    print('Final estimate using square_root_while is {0}'.format(x_final))
