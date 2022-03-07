
import requests
import numpy as np
from sklearn.linear_model import LinearRegression



## Function A
def function_A(n):
    pi_2 = 1
    nom, den = 2.0, 1.0
    for i in range(n):
        pi_2 *= nom / den
        if i % 2:
            nom += 2
        else:
            den += 2      
    return 2*pi_2


## Function B
def function_B(ping_url):
  return requests.get(ping_url) # Retrieve a single page and report the URL and contents


## curve_fit()

# We define the sigmoid function 
def sigmoid(x, a, b, c, d):
    return a * 1/(1+np.exp(-b*x+c))+d # we consider here amplitude, slope, shift and relative shift.

def variables(s=20, n = 10):
    x = np.arange(-s//2, s//2, .1)       # Array for x-axis   
    y = sigmoid(x, 1, 2.1, 3.3, 0)  # Creating a sigmoid using some given values and the x-array
    #########
    ## Generate some fake measurements from experiment
    #########
    ydata = [y+y_noise for y_noise in 0.1 * np.random.randn(n,y.size)]   # Adding noise to the original sigmoid function

    return x, y, ydata



## Linear Regression

def linearFunction(x, m, b):
    return m*x+b

def variables2(m = 2, b = 1, s=20, n = 10):
    x = np.arange(-s//2, s//2, .1)
    y = linearFunction(x,m,b)  # Creating a line using your function and the values given
    ydata = [y+y_noise for y_noise in 0.5 * np.random.randn(n,y.size)] # Adding noise to the original linear function
    return x, y, ydata

def lin_reg(x, yn):
    X = x.reshape((-1, 1))
    reg = LinearRegression()
    reg.fit(X, yn)
    return reg.predict(X) 


