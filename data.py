import numpy as np
class Data:
    def __init__(self, x, y):
        """ (Data, list, list) -> NoneType

        Create a new data object with two attributes: x and y.
        """
        self.x=x
        self.y=y

    def num_obs(self):
        """ (Data) -> int

        Return the number of observations in the data set.

        >>> data = Data([1, 2], [3, 4])
        >>> data.num_obs()
        2
        """
        return len(self.x)

    def __str__(self):
        """ (Data) -> str
        Return a string representation of this Data in this format:
        x	        y
        18.000          120.000
        20.000          110.000
        22.000          120.000
        25.000          135.000
        26.000          140.000
        29.000          115.000
        30.000          150.000
        33.000          165.000
        33.000          160.000
        35.000          180.000
        >>> dat = Data([1,2,3],[2,4,6])
        >>> print(dat)
        x y
        1.000 2.000
        2.000 4.000
        3.000 6.000
        """
        prints = 'x y'
        for i in range(len(self.x)):
            prints = prints + '\n' + str(format(self.x[i],".3f")) + ' ' + str(format(self.y[i],".3f")) 
        return prints
    
    def compute_sample_means(self):
        """ (Data) -> number, number

        Return sample mean of x and sample mean of y.
        """
        meanx = sum(self.x)/len(self.x)
        meany = sum(self.y)/len(self.y)
        return (meanx, meany)


    def compute_least_squares_fit(self):
        """ (Data) -> number, number

        Return the intercept and slope of the simple linear regression fit
        of the data.
        """
        n = self.num_obs()
        Sxx1 = [0]*n
        Sxy1 = [0]*n
        for i in range(n):
            Sxx1[i] = self.x[i] * self.x[i]
            Sxy1[i] = self.x[i] * self.y[i]
        sx = sum(self.x)
        sy = sum(self.y)
        Sxx=sum(Sxx1)
        Sxy=sum(Sxy1)
        slope1=(n * Sxy)- (sx * sy)
        slope2=(n * Sxx) - (sx**2)
        slope=slope1 / slope2
        intercept= (sy - slope * sx)/n
        return (intercept,slope)


    def compute_SST(self):
        """ (Data) -> number

        Return the sum of squares total (SST).
        """
        n = self.num_obs()
        u=np.array(self.y)
        SST=np.sum(u**2)- 1/n*(np.sum(u))**2
        return SST

    
    
    