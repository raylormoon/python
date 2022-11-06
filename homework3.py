
# Name: Tianjjiao Xu

import math
# Problem 1.
cities={}

cities['Raleigh'] = (35.7796, -78.6382)
cities['Tianjin'] = (39.129498, 117.251038)
cities['Centreville'] = (32.9446, -87.1386)
cities['Los Angeles']=(34.0522, -118.2437)
cities['Houston']=(29.749907, -95.258421)


# Problem 2.
def degrees_to_radians(degree):
    """
    >>> degrees_to_radians(60)
    1.0471975511965976
    
    >>> degrees_to_radians(90)
    1.5707963267948966
    
    Parameters
    ----------
    degree : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    if degree>=-180 and degree<=180:
        return degree*(math.pi/180)

    else:
        print('Error')
        return
    
# Problem 3.

def distance_great_circle(points,R):
    """
    >>> distance_great_circle([[-1,1],[-2,2]],6371)
    5552.461787341514
    
    Parameters
    ----------
    points : TYPE
        DESCRIPTION.
    R : 
        DESCRIPTION.

    ReturnsTYPE
    -------
    TYPE
        DESCRIPTION.

    """
    phi1= points[0][0]
    phi2= points[1][0]
    lamda1=points[0][1]
    lamda2=points[1][1]

    if R>=0: 
        x=(math.sin((phi2-phi1)/2))**2+math.cos(phi1)*math.cos(phi2)*(math.sin((lamda2-lamda1)/2))**2
        distance_great_circle = math.asin(math.sqrt(x))*(2*R)
        return distance_great_circle
    else:
        return False
    
# Problem 4.

def polar_to_cartesian(latlon,R):
    polar=latlon[0]
    alpha=latlon[1]
    
    if R>=0:
        x = R * math.cos(polar) * math.cos(alpha)
        y = R * math.cos(polar) * math.sin(alpha)
        z = R * math.sin(polar)
        return(x,y,x)
    else:
        return False

# Problem 5.
def distance_Euclidean(points,R):
    x1=points[0][0]
    y1=points[0][1]
    x2=points[1][0]
    y2=points[1][1]
           
    if R>=0:
        a1 = R * math.cos(x1) * math.cos(y1)
        b1 = R * math.cos(x1) * math.sin(y1)
        c1 = R * math.sin(x1)
        a2 = R * math.cos(x2) * math.cos(y2)
        b2 = R * math.cos(x2) * math.sin(y2)
        c2 = R * math.sin(x2)
        distance_Euclidean = math.sqrt(math.pow((a1-a2),2) + math.pow((b1-b2),2) + math.pow((c1-c2),2))
        return distance_Euclidean
    
    else:
        return False

# Problem 6.

def distances(city1,city2,cities):
    if city1 in cities and city2 in cities:
        return distance_great_circle([cities[city1],cities[city2]],6371),distance_Euclidean([cities[city1],cities[city2]],6371)
    else:
        return ((math.nan),(math.nan))

# Problem 7.

def summarize_distances(city1,city2,cities):
    if city1 in cities and city2 in cities:
        s1='The great circle distance is {:.2f} km and the Euclidean distance is {:.2f} km.'.format(distance_great_circle([cities[city1],cities[city2]],6371),distance_Euclidean([cities[city1],cities[city2]],6371))
        return s1
    else:
        return 'Error: either city1 or city2 is missing from cities.'


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(degrees_to_radians(60))
    print(degrees_to_radians(90))
    print(distance_great_circle([[10,-10],[20,-20]],6371))
    print(distance_great_circle([[10,-10],[30,-20]],6371))
    print(polar_to_cartesian((10,-10),6371))
    print(polar_to_cartesian((10,-20),6371))
    print(distance_Euclidean([[10,-10],[20,-20]],6371))
    print(distance_Euclidean([[10,-10],[30,-20]],6371))
    
    
