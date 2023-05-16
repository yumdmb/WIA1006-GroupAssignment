import numpy as np
#Test the model
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt
from LinearRegression import LinearRegression

X, y = datasets.make_regression(n_samples=100, n_features=1, noise=20, random_state=4)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

fig=plt.figure(figsize=(8,6))
plt.scatter(X[:, 0], y, color="b", marker="o", s=30)
plt.show()

reg = LinearRegression()
reg.fit(X_train,y_train)
predictions = reg.predict(X_test)

def mse(y_test, predictions):
    return np.mean((y_test-predictions)**2)


mse=mse(y_test,predictions)
print(mse)

y_pred_line = regressor.predict(X)
cmap - plt.get_cmap('viridis')
fig=plt.figure(figsize=(8,6)