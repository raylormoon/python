#Collaborators:
## Please list all sources, including those outside of class like StackExchange.
##codingem 

import numpy as np
import matplotlib.pyplot as plt
import math
## 1. Complete sort_data

def sort_data(data):
    """ (tuple) -> tuple
    
    data is a tuple of two lists.
    
    Returns a copy of the input tuple sorted in
    non-decreasing order with respect to the 
    data[0]
    
    >>> sort_data(([5, 1, 7], [1, 2, 3]))
    ([1, 5, 7], [2, 1, 3])

    >>> sort_data(([2, 4, 8], [1, 2, 3]))
    ([2, 4, 8], [1, 2, 3])

    >>> sort_data( ([11, 4, -5], [1, 2, 3]))
    ([-5, 4, 11], [3, 2, 1])
    """
    
    xco = data[0]
    yco = data[1]
    indices = np.argsort(xco) 
    return ([xco[a] for a in indices],[yco[b] for b in indices])
    

## 2. Complete find_index

def find_index(x, x_new):
    """ (list, number) -> int
    
    Returns the smallest index i such that x[i] <= x_new 
    and x[i+1] >= x_new.
    
    Assumes i) there are no duplicated values in x,
    ii) x is sorted in ascending order, and
    iii) x_new falls between min(x) and max(x).
    
    >>> find_index([1, 5, 7, 9], 1)
    0

    >>> find_index([1, 5, 7, 9], 2)
    0

    >>> find_index([1, 5, 7, 9], 6)
    1

    >>> find_index([1, 5, 7, 9], 7)
    1

    >>> find_index([1, 5, 7, 9], 8)
    2

    >>> find_index([1, 5, 7, 9], 9)
    2
    """
    for i in range(len(x)-1):
        if x[i+1] >= x_new >= x[i]:
            return i
        
## 3. Complete linear_predict

def linear_predict(data, x_new):
    """ (tuple, number) -> number
    
    data is a tuple.
    
    data[0] are the x coordinates and 
    data[1] are the y coordinates.

    Returns linearly interpolated value at x_new.
    
    Assumes i) there are no duplicated values in data[0],
    ii) data[0] is sorted in ascending order, and
    iii) x_new falls between min(x) and max(x).
        
    >>> linear_predict(([0, 5, 10], [1, 7, -5]), 2)
    3.4
    
    >>> linear_predict(([0, 5, 10], [1, 7, -5]), 9)
    -2.5999999999999996
    
    """
    x = data[0]
    y = data[1]
    i=find_index(x,x_new)
    a=(y[i+1]-y[i])/(x[i+1]-x[i])
    y_new=y[i]+a*(x_new-x[i])
    return y_new
    

## 4. Complete linear_interpolate

def linear_interpolate(data, x_new_list):
    """ (tuple, list) -> list

    data is a tuple.
    
    data[0] are the x coordinates and 
    data[1] are the y coordinates.
    
    Returns linearly interpolated value at x_new_list.
    
    Assumes i) there are no duplicated values in data[0],
    ii) data[0] is sorted in ascending order, and
    iii) items in x_new_list fall between min(x) and max(x).    
    
    >>> linear_interpolate(([0, 5, 10], [1, 7, -5]), [2, 9])
    [3.4, -2.5999999999999996]
    """
    mylist=[]
    for i in range(len(x_new_list)):
        mylist.append(linear_predict(data, x_new_list[i]))           
    return mylist

    
## 5. Complete kernel_predict
def k(u,v,h):
    return math.exp((u-v)**2/(h*-2))

def wi(x,x_new,xi,h):
    pa=k(x_new,xi,h)
    pab=0
    for i in range(len(x)):
        pab+=k(x_new,x[i],h)
    return pa/pab

def kernel_predict(data, x_new, h):
    """ (tuple, number, number) -> number

    data is a tuple.
    
    data[0] are the x coordinates and 
    data[1] are the y coordinates.
    
    h is a positive bandwidth parameter.
    
    Returns Nadarayan-Watson estimate using bandwith
    parameter h at x_new.
    
    Assumes i) there are no duplicated values in data[0],
    ii) data[0] is sorted in ascending order, and
    iii) x_new falls between min(x) and max(x).
    
    >>> kernel_predict(([0, 5, 10], [1, 7, -5]), 2, 6)
    3.3499798573575896
    
    >>> kernel_predict(([0, 5, 10], [1, 7, -5]), 7, 6)
    2.2150028476392194
    """
    
    y_new=0#start from 0
    wi_sum = 0
    for i in range(len(data[0])):
        wi_sum+=wi(data[0],x_new,data[0][i],h)
        y_new+=data[1][i]*(wi(data[0],x_new,data[0][i],h))
    return y_new/wi_sum

## 6. Complete kernel_smooth

def kernel_smooth(data, x_new_list, h):
    """ (tuple, list, number) -> list

    data is a tuple.
    
    data[0] are the x coordinates and 
    data[1] are the y coordinates.
    
    h is a positive bandwidth parameter.
    
    Returns list of Nadarayan-Watson estimates using
    bandwith parameter h at items in x_new_list.
    
    Assumes i) there are no duplicated values in data[0],
    ii) data[0] is sorted in ascending order, and
    iii) items in x_new_list fall between min(x) and max(x).      
    
    >>> kernel_smooth(([0, 5, 10], [1, 7, -5]), [2, 7], 6)
    [3.3499798573575896, 2.2150028476392194]
    """
    
    ylist=[]
    for i in x_new_list:
        ylist.append(kernel_predict(data, i, h))         
    return ylist

## 7. Complete knn_predict

def knn_predict(data, x_new, k):
    """ (tuple, number, int) -> number

    data is a tuple.
    
    data[0] are the x coordinates and 
    data[1] are the y coordinates.
    
    k is a positive nearest neighbor parameter.
    
    Returns k-nearest neighbor estimate using nearest
    neighbor parameter k at x_new.
    
    Assumes i) there are no duplicated values in data[0],
    ii) data[0] is sorted in ascending order, and
    iii) x_new falls between min(x) and max(x).
    
    >>> knn_predict(([0, 5, 10, 15], [1, 7, -5, 11]), 2, 2)
    4.0
    
    >>> knn_predict(([0, 5, 10, 15], [1, 7, -5, 11]), 2, 3)
    1.0

    >>> knn_predict(([0, 5, 10, 15], [1, 7, -5, 11]), 8, 2)
    1.0

    >>> knn_predict(([0, 5, 10, 15], [1, 7, -5, 11]), 8, 3)
    4.333333333333333
    """
    new_data = list(data)
    new_data[0] = [abs(i - x_new) for i in data[0]]
    sort_new_data = sort_data(new_data)
    my_k=0
    res = 0
    while my_k<k:
        res += sort_new_data[1][my_k]
        my_k += 1
    return res / k

## 8. Complete def knn_smooth

def knn_smooth(data, x_new_list, k):
    """ (tuple, list, int) -> number

    data is a tuple.
    
    data[0] are the x coordinates and 
    data[1] are the y coordinates.
    
    k is a positive nearest neighbor parameter.
    
    Returns list of k-nearest neighbor estimates using
    nearest neighbor parameter k at items x_new_list.
    
    Assumes i) there are no duplicated values in data[0],
    ii) data[0] is sorted in ascending order, and
    iii) items in x_new_list fall between min(x) and max(x).      
        
    >>> knn_smooth(([0, 5, 10, 15], [1, 7, -5, 11]), [2, 8], 2)
    [4.0, 1.0]
    
    >>> knn_smooth(([0, 5, 10, 15], [1, 7, -5, 11]), [2, 8], 3)
    [1.0, 4.333333333333333]
    """
    zlist=[]
    for i in range(len(x_new_list)):
       y_value=knn_predict(data, x_new_list[i], k)
       zlist.append(y_value)
    return zlist

## 9. Complete my_median

def my_median(x):
    """ (list) -> float

    Computes the median as a float of a list of numbers.

    >>> my_median([1, 2, 3])
    2.0

    >>> my_median([1, 2, 3, 4])
    2.5
    """
    a=sorted(x)
    n = len(x)
    if n%2==0:
        return float((a[n//2-1]+a[n//2])/2.0)
    else:
        return float(a[(n+1)//2-1])

## 10. Complete median_filter

def median_filter(y, W):
    """ (list, int) -> list
    
    Returns a list whose ith item is
    the median value of y[start:stop+1] where
    start is the larger of 0 and i - W and
    stop is the smaller of i + W and n-1.
    
    >>> median_filter([-1.0, 6.0, 7.0, -2.0, 0.0, 8.0, 13.0], 1)
    [2.5, 6.0, 6.0, 0.0, 0.0, 8.0, 10.5]
    """
    
    n = len(y)
    a = []
    b = []
    for i in range(W+1):
        if(i<n):
            b.append(y[i])
    for i in range(n):
        a.append(my_median(b))
        next = i+W+1
        prev = i-W
        if(next<n):
            b.append(y[next]) 
        if(prev>=0):
            b.pop(0)
    return a

## 11. Complete smoother

def smoother(data, x_new_list, method = 'interpolate', filter_flag = False, W = 5, h = 1, k = 1):
    """ (tuple, list, str, bool, int, number, int) -> list

    Wrapper function for three snoothing operations.
    
    1. Linear interpolation (method='interpolate')
    2. Gaussian kernel smoothing (method='kernel')
    3. k-nearest-neighbor smoothing (method='knn')
    
    filter_flag is a Boolean variable. If True,
    median_filter is applied prior to smoothing.
        
    data is a tuple.
    
    data[0] are the x coordinates and 
    data[1] are the y coordinates.

    W is a positive window parameter used in median_filter
    
    h is a positive bandwidth parameter used in kernel_smooth.
    
    k is a positive nearest neighbor parameter used in knn_smooth.
    
    See linear_interpolate, kernel_smooth, and knn_smooth
    for details.

    Assumes i) there are no duplicated values in data[0],
    ii) items in x_new_list fall between min(x) and max(x).
    """
    data=sort_data(data)
    if method == 'interpolate':
         if filter_flag is False:
            return linear_interpolate(data, x_new_list)
         if filter_flag is True:
            a=median_filter(data[1], W)
            b=[data[0],a]
            return linear_interpolate(b, x_new_list)
        
    if method == 'kernel':
         if filter_flag is False:
            return kernel_smooth(data, x_new_list, h)
         if filter_flag is True:
             a=median_filter(data[1], W)
             b=[data[0],a]
             return kernel_smooth(b, x_new_list, h)
        
    if method == 'knn':
         if filter_flag is False:
            return knn_smooth(data, x_new_list, k)
         if filter_flag is True:
             a=median_filter(data[1], W)
             b=[data[0],a]
             return knn_smooth(b, x_new_list, k)
    else:
         print('Unsupported method.' )
         return None
    
## 12. Make plots

days = [22, 20, 1, 42, 29, 6, 33, 34, 39, 46, 12, 38, 17, 49, 7, 11, 48, 18, 31, 23, 27, 37, 44, 16, 36, 24, 30, 2, 13, 32, 4, 14, 15, 35, 45, 41, 19, 47, 28, 43, 3, 40, 50, 26, 5, 9, 8, 25, 21, 10]
AQI = [2.2, 2.9, 2.6, 2.7, 1, 1.2, 0.8, 0.6, 2.7, 3.9, 0.7, 3.1, 1.5, 4.4, 1.2, 0.7, 6.6, 1.6, 1.9, 2.9, 3.9, 4.4, 2.8, 1.7, 1.4, 4.8, 1.7, 2, 1.1, 1.4, 2.2, 2, 2.2, 0.8, 2.4, 2.5, 1.9, 3.7, 1.5, 2.9, 2.2, 2.1, 3.5, 6.1, 1.6, 0.9, 1, 6.9, 2.2, 0.6]
AQI_data = (days, AQI)

x_new_list=np.linspace(1,50,100)
AQI_data=sort_data(AQI_data)

## 1a.
dataa=smoother(AQI_data, x_new_list, method = 'interpolate', filter_flag = False, W = 5, h = 1, k = 1)
plt.plot(x_new_list,dataa,'g--')
plt.plot(days,AQI,'ks',markersize=5)
plt.show()
## 1b.
datab=smoother(AQI_data, x_new_list, method = 'kernel', filter_flag = False, W = 5, h = 0.1, k = 1)
plt.plot(x_new_list,datab,'b-')
databa=smoother(AQI_data, x_new_list, method = 'kernel', filter_flag = False, W = 5, h = 1, k = 1)
plt.plot(x_new_list,databa,'g-')
databb=smoother(AQI_data, x_new_list, method = 'kernel', filter_flag = False, W = 5, h = 10, k = 1)
plt.plot(x_new_list,databb,'m-')
plt.plot(days,AQI,'ks',markersize=5)
plt.show()

## 1c.
dataaa=smoother(AQI_data, x_new_list, method = 'knn', filter_flag = False, W = 5, h = 1, k = 1)
plt.plot(x_new_list,dataaa,'b-')
databaa=smoother(AQI_data, x_new_list, method = 'knn', filter_flag = False, W = 5, h = 1, k = 5)
plt.plot(x_new_list,databaa,'g-')
databba=smoother(AQI_data, x_new_list, method = 'knn', filter_flag = False, W = 5, h = 1, k = 15)
plt.plot(x_new_list,databba,'m-')
plt.plot(days,AQI,'ks',markersize=5)
plt.show()

## 2a.
datad=smoother(AQI_data, x_new_list, method = 'interpolate', filter_flag = True, W = 5, h = 1, k = 1)
plt.plot(x_new_list,datad,'g--')
plt.plot(days,AQI,'ks',markersize=5)
plt.show()

## 2b.
dataz=smoother(AQI_data, x_new_list, method = 'kernel', filter_flag = True, W = 5, h = 0.1, k = 1)
plt.plot(x_new_list,dataz,'b-')
dataza=smoother(AQI_data, x_new_list, method = 'kernel', filter_flag = True, W = 5, h = 1, k = 1)
plt.plot(x_new_list,dataza,'g-')
datazb=smoother(AQI_data, x_new_list, method = 'kernel', filter_flag = True, W = 5, h = 10, k = 1)
plt.plot(x_new_list,datazb,'m-')
plt.plot(days,AQI,'ks',markersize=5)
plt.show()

## 2c.
datay=smoother(AQI_data, x_new_list, method = 'knn', filter_flag = True, W = 5, h = 1, k = 1)
plt.plot(x_new_list,datay,'b-')
databy=smoother(AQI_data, x_new_list, method = 'knn', filter_flag = True, W = 5, h = 1, k = 5)
plt.plot(x_new_list,databy,'g-')
databby=smoother(AQI_data, x_new_list, method = 'knn', filter_flag = True, W = 5, h = 1, k = 15)
plt.plot(x_new_list,databby,'m-')
plt.plot(days,AQI,'ks',markersize=5)
plt.show()

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
    
#I think the most interting part is the plots. I think igot it when i am in class. 
#But i am not so it make me learn a lot. I like knn smooth best and kernel least.
#I am prond of i start early so i have time to ask teachers and tas.
