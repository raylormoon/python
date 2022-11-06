
# Name: tianjiao Xu

# Problem 1.
import math
import numpy as np

def gaussian(x):
    
    """
    >>> gaussian(2)
    0.05399096651318806
    
    >>> gaussian(3)
    0.004431848411938008
    
    Parameters
    ----------
    x : TYPE
        DESCRIPTION.

    Returns
    -------
    f_x : TYPE
        DESCRIPTION.

    """
    f_x_part1=1/math.sqrt(2*math.pi)
    f_x_part2=math.pow(math.e,-x**2/2)
    f_x=f_x_part1*f_x_part2
    return f_x


# Problem 2.

def under_curve(x, y):
    """
    >>> under_curve(2,3)
    False
    
    >>> under_curve(0,0)
    True
    
    Parameters
    ----------
    x : TYPE
        the value of x-axis
    y : TYPE
        the value of y-axis

    Returns
    -------
    bool
        point under the curve or not

    """
    f_x=gaussian(x)
    if 0<=y<=f_x:
        return True
    else:
        return False

    
# Problem 3.

def greater_than(x, a):
    """
    >>> greater_than(2,3)
    False
    
    >>> greater_than(3,2)
    True

    Parameters
    ----------
    x : TYPE
        the value of x_axis
    a : TYPE
        the max value

    Returns
    -------
    None.

    """
    if x>a:
        return True
    else:
        return False


# Problem 4.

def less_than(x, b):

    """
    >>> less_than(2, 3)
    True
    
    >>> less_than(3, 2)
    False

    Parameters
    ----------
    x : TYPE
        
    b : TYPE
        

    Returns
    -------
    None.

    """
    if x<b:
        return True
    else:
        return False

# Problem 5.

def monte_carlo_gaussian(a, b, n):
    """

    Parameters
    ----------
    a : TYPE
        max value
    b : TYPE
        nimi value
    n : TYPE
        size

    Returns
    -------
    area : TYPE
        the area of the curve

    """
    xy_min = [a, 0]
    xy_max = [b, 1/math.sqrt(2*math.pi)]   
    samples = np.random.uniform(low=xy_min, high=xy_max, size=(n, 2))
    count_under_area = 0
    for i in range(n):
        data_point = samples[i]
        if under_curve(data_point[0], data_point[1]):
             count_under_area = count_under_area + 1
    p=count_under_area/n
    area=p*(b-a)*(1/math.sqrt(2*math.pi)) 
    return area


# Problem 6. Print out estimates for different numbers of darts thrown.
print(monte_carlo_gaussian(-1.645,1.645,10))
print(monte_carlo_gaussian(-1.645,1.645,100))
print(monte_carlo_gaussian(-1.645,1.645,1000))
print(monte_carlo_gaussian(-1.645,1.645,10000))




if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
    print(gaussian(2))
    print(gaussian(3))
    print(under_curve(2,3))
    print(under_curve(0,0))
    print(greater_than(2,3))
    print(greater_than(3,2))
    print(less_than(2, 3))
    print(less_than(3,2))
