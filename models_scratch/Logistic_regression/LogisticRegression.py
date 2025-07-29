#!/usr/bin/env python
# coding: utf-8

# # Logistic Regression

# ### It predicts whether something is true or false, instead of something continious

# **Although logistic regression tells the probability that a mouse is obese or not, its usually used for classifications**

# If probability of something is > 50% then it will be considered as True, else False

# eg: Obesity is predicted by weight

# it can also be used to asses what variables are useful for classify samples.

# we can do logistic regression on continious(like weights) and discrete variable(gender), for continious variables it is related to linear regression 

# **The curve that fits for logistic regression is the similar to sigmoid function curve (1/(1+e^x)) and for best fitting we minimize the cost function for this**

# while for the linear regression the cost function was just mean square error, but that will suit for continious variable but here our output can only be binary

# While linear regression uses mean square error as its cost function—appropriate for continuous variables, logistic regression handles binary outputs so has a different cost function.
# 
# First see if it has the same cost function as linear regression then by gradient descent we will not be sure to reach global minima while minimizing it instead might stuck at local minima.
# 
# **Cost = -1/m[sum(ylog(y’) + (1-y)log(1-y’))]**
# 
# where y’ = sigmoid(w.T * X + b)
# 
# now to get the best fit for the curve we will minimize the cost function and use gradient descent in which
# 
# w = w - (learning rate)*(d(cost)/dw)
# 
# b = b - (learning rate)*(d(cost)/db)
# 
# the derivatives to minimize will be 
# 
# d(cost)/dw = -W/m * sum(y - y’)
# 
# d(cost)/db = -1/m * sum(y - y’)
# 
# then we would have our best fitting curve and the model ready

# In[2]:


## Implementing Logistic Regression


# In[9]:


import numpy as np


# In[10]:


def sigmoid(x):
        return 1/(1 + np.exp(-x))


# In[11]:


class LogisticRegression:

    def __init__(self, lr = 0.01, n_iters = 1000):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None


    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iters):
            y_line = np.dot(X, self.weights) + self.bias

            y_pred = sigmoid(y_line)
    
            dw = 1/n_samples * np.dot(X.T, (y_pred - y))
            db = 1/n_samples * np.sum(y_pred - y)
    
            self.weights = self.weights - self.lr * dw
            self.bias = self.bias - self.lr * db

    def predict(self, X):
        y_line = np.dot(X, self.weights) + self.bias
        y_pred = sigmoid(y_line)

        class_pred = [0 if y < 0.5 else 1 for y in y_pred]
        return class_pred
        
        


# In[ ]:





# In[ ]:




