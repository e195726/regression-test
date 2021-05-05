import datasets
X,Y = datasets.load_linear_example1()

print(X)

print(X[0])

print(Y)

import regression
model = regression.LinearRegression()

import importlib
importlib.reload(regression)
model = regression.LinearRegression()
model.fit(X,Y)
print(model.theta)

import importlib
importlib.reload(regression)
model = regression.LinearRegression()
model.fit(X,Y)
print(model.predict(X))
