import numpy as np
from scipy import stats
from data import Data
import matplotlib.pyplot as plt
from read_data import read_data

class SLR:
    def __init__(self, data):
        """ (SLR, Data) -> NoneType

        Create a new simple linear regression object from data,
        with data data, intercept beta0, and slope beta1.
        """
        self.data=data
        (self.beta0 , self.beta1) = data.compute_least_squares_fit()
        
    def predict(self, x_new):
        """ (SLR, number) -> number

        Return predicted value at x_new.
        """
        return self.beta0 + self.beta1 * x_new 
        
    def compute_residuals(self):
        """ (SLR) -> list

        Return the residuals in a list of numbers.
        """
        SLR=[]
        n=self.data.num_obs()
        for i in range(n):
            SLR.append(self.data.y[i]-self.predict(self.data.x[i]))
        return SLR
    
    def compute_SSResid(self):
        """ (SLR) -> number

        Return the sum of square residuals (SSResid).
        """
        res = self.compute_residuals()
        SSResid = 0
        for i in range(len(res)):
            SSResid = SSResid + (res[i] ** 2)
        return SSResid
    
    
    def compute_residual_sd(self):
        """ (SLR) -> number

        Return the residual standard deviation.
        """
        n=self.data.num_obs()
        return (self.compute_SSResid()/(n- 2))**0.5
    
    def compute_rsquared(self):
        """ (SLR) -> number

        Return the R-squared of the SLR fit.
        """
        a=self.data.compute_SST()
        b=self.compute_SSResid()
        return (a - b) / a
    
    
    def __str__(self):
        """ (SLR) -> str

        Return a string representation of an SLR in this format:

        Least squares fit on 10 data points.
        Intercept = 45.584331
        Slope = 3.465523
        Residual standard deviation = 13.051139
        R-squared = 0.731364
        """
        return 'Least squares fit on {} data points.\nIntercept = {:.6f}\nSlope = {:.6f}\nResidual standard deviation = {:.6f}\nR-squared = {:.6f}'.format(self.data.num_obs(),self.beta0,self.beta1,self.compute_residual_sd(),self.compute_rsquared())

    def plot(self):
        """ (SLR) -> None

        Produce a scatter plot of the data and
        the simple linear regression model.
        """
        x = np.linspace(600, 1100, 1000)
        plt.plot(self.data.x, self.data.y, 'b^')
        plt.plot(x,self.beta0 + self.beta1 * x, linestyle='solid',color ='black')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
        return

a,b=read_data('area_bill.csv') 
dat=Data(a,b)
lm=SLR(dat)
print(lm)
print(lm.plot())


c,d=read_data('wt_vs_mpg.csv') 
dat=Data(c,d)
lm=SLR(dat)
print(lm)









