## Collaborators:
## Please list all sources, including those outside of class like StackExchange.


import os.path
import pandas as pd

def read_data(input_file_name):
    """ (str) -> list, list

    Read data from the path specified by the string input_file.
    Data looks like:

    18,  120
    20,  110
    22,  120
    25,  135

    Output two lists, one for each column of data.
    """
    try:
        data = pd.read_csv(input_file_name,index_col=False, names=['x','y']) 
            
        x =list(data['x'])
        y = list(data['y'])
        return(x,y)
    except:
        print('Unable to open and read my_file.txt')
        return None,None

os.getcwd()
x,y=read_data('area_bill.csv')     
print(x,y)
x1,y1=read_data('wt_vs_mpg.csv')     
print(x1,y1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        