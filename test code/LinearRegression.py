import numpy as np

class LinearRegression:
    
    def __init__(self, lr=0.001, n_iters=1000):
        self.lr=lr
        self.n_iters=n_iters
        self.weights= None
        self.bias = None

    # init weight=0 ,bias=0 #1 weight/feature
    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        #update weight and bias : w=w-a.dw and b=b-a.db ;a is learning rate
        for _ in range(self.n_iters):
            y_pred = np.dot(X, self.weights) + self.bias # predict result using y=wx+b (in array)
            
            dw = (1/n_samples)*np.dot(X.T, (y_pred-y))
            db = (1/n_samples)*np.sum(y_pred-y)

            #update w and b
            self.weights = self.weights - self.lr*dw
            self.bias = self.bias - self.lr*db

    def predict(self, X):
        y_pred = np.dot(X, self.weights) + self.bias
        return y_pred   