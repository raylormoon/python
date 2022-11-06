# Name:Tianjiao Xu


import math
def standard_error(x1,x2,x3,x4):
    a=math.pow(x1-(x1+x2+x3+x4)/4,2)
    b=math.pow(x2-(x1+x2+x3+x4)/4,2)
    c=math.pow(x3-(x1+x2+x3+x4)/4,2)
    d=math.pow(x4-(x1+x2+x3+x4)/4,2)
    return math.sqrt((1.3)*(a+b+c+d))/math.sqrt(4)

# Problem 1.

def t_test_two_tailed(x1,x2,x3,x4,mu,cl):
    
    """
    >>> t_test_two_tailed(1,2,3,4,5,90)
    There is not a statistically significant difference at the 90% confidence level.

    Parameters
    ----------
    x1 : TYPE
        DESCRIPTION.
    x2 : TYPE
        DESCRIPTION.
    x3 : TYPE
        DESCRIPTION.
    x4 : TYPE
        DESCRIPTION.
    mu : TYPE
        DESCRIPTION.
    cl : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    x_bar=(x1+x2+x3+x4)/4
    t=(x_bar-mu)/standard_error(x1, x2, x3, x4)
    
    if cl!=90 and cl!=95 and cl!=99:
       print('That confidence level is not supported')
       return('That confidence level is not supported')
   
    
    if cl==99:
       if abs(t)>5.84:
          print('There is a statistically significant difference at the 99% confidence level.')
       else:
          print('There is not a statistically significant difference at the 99% confidence level.')
       return


    if cl==95:
       if abs(t)>3.18:
          print('There is a statistically significant difference at the 95% confidence level.')
       else:
          print('There is not a statistically significant difference at the 95% confidence level.')
       return
   
    if cl==90:
       if abs(t)>2.35:
          print('There is a statistically significant difference at the 90% confidence level.')
       else:
          print('There is not a statistically significant difference at the 90% confidence level.')
       return

    
# Problem 2.

def t_test_lower_tailed(x1,x2,x3,x4,mu,cl):
    """
    >>> t_test_lower_tailed(1,2,3,4,5,95)
    There is not a statistically significant difference at the 95% confidence level.

    Parameters
    ----------
    x1 : TYPE
        DESCRIPTION.
    x2 : TYPE
        DESCRIPTION.
    x3 : TYPE
        DESCRIPTION.
    x4 : TYPE
        DESCRIPTION.
    mu : TYPE
        DESCRIPTION.
    cl : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    x_bar=(x1+x2+x3+x4)/4
    
    t=(x_bar-mu)/standard_error(x1, x2, x3, x4)
    
    
    if cl!=90 and cl!=95 and cl!=99:
       print('That confidence level is not supported')
       return('That confidence level is not supported')
   
    
    if cl==99:
       if t<-4.54:
          print('There is a statistically significant difference at the 99% confidence level.')
       else:
          print('There is not a statistically significant difference at the 99% confidence level.')
       return


    if cl==95:
       if t<-2.35:
          print('There is a statistically significant difference at the 95% confidence level.')
       else:
          print('There is not a statistically significant difference at the 95% confidence level.')
       return
   
    if cl==90:
       if t<-1.64:
          print('There is a statistically significant difference at the 90% confidence level.')
       else:
          print('There is not a statistically significant difference at the 90% confidence level.')
       return
    
    

# Problem 3.

def t_test_upper_tailed(x1,x2,x3,x4,mu,cl):
    """
    >>> t_test_two_tailed(1,2,3,4,5,99)
    There is not a statistically significant difference at the 99% confidence level.
    
    Parameters
    ----------
    x1 : TYPE
        DESCRIPTION.
    x2 : TYPE
        DESCRIPTION.
    x3 : TYPE
        DESCRIPTION.
    x4 : TYPE
        DESCRIPTION.
    mu : TYPE
        DESCRIPTION.
    cl : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    x_bar=(x1+x2+x3+x4)/4
    
    t=(x_bar-mu)/standard_error(x1, x2, x3, x4)
    
    
    if cl!=90 and cl!=95 and cl!=99:
       print('That confidence level is not supported')
       return('That confidence level is not supported')
   
    
    if cl==99:
       if t>4.54:
          print('There is a statistically significant difference at the 99% confidence level.')
       else:
          print('There is not a statistically significant difference at the 99% confidence level.')
       return


    if cl==95:
       if t>2.35:
          print('There is a statistically significant difference at the 95% confidence level.')
       else:
          print('There is not a statistically significant difference at the 95% confidence level.')
       return
   
    if cl==90:
       if t>1.64:
          print('There is a statistically significant difference at the 90% confidence level.')
       else:
          print('There is not a statistically significant difference at the 90% confidence level.')
       return


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
    print(t_test_two_tailed(1,2,3,4,5,90))
    print(t_test_upper_tailed(1,2,3,4,5,99))
    print(t_test_lower_tailed(1,2,3,4,5,95))
