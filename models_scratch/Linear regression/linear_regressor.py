#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


class LinearRegression:

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
            y_pred = np.dot(X, self.weights) + self.bias # This is the Model y = wX + b but for all the samples at the same time by vectors
            #calculation of error to use in gradient descent
            dw = (1/n_samples) * np.dot(X.T, (y_pred - y))
            db = (1/n_samples) * np.sum(y_pred - y)
    
            self.weights = self.weights - self.lr * dw
            self.bias = self.bias - self.lr * db
        
        


    def predict(self, X):
        y_pred = np.dot(X, self.weights) + self.bias

        return y_pred
        
        


# In[ ]:




