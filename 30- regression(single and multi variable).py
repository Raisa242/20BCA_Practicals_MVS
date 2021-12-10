# -*- coding: utf-8 -*-
"""


@author: sanjay
"""

# EDA and linear regression for two pair of variables
import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import datasets
import sklearn



os.chdir("C:/Users/sanjay/Documents")
car=pd.read_csv('CarPrice_Assignment.csv')
#print(car.describe())
car.info()

# 1. EDA and visualisation 

print(car.describe())

sns.countplot('doornumber',data=car)
plt.show()

plt.hist('cylindernumber',data = car)
plt.show()

x= car.corr(method= 'pearson')
print(x)

sns.heatmap(car.corr(method='pearson').drop(['car_ID','symboling'],axis=1).drop(['car_ID','symboling'],axis=0),data=car)
sns.show()

df = pd.DataFrame(car,columns=['cylindernumber','horsepower'])
plt.bar(df['cylindernumber'], df['horsepower'])
plt.title('Cylinder number vs Horsepower', fontsize=14)
plt.xlabel('CYlinder Number', fontsize=14)
plt.ylabel('Horse Power', fontsize=14)
plt.show()


sns.pairplot(car)
plt.show()

sns.boxplot(y='compressionratio',x='fueltype',data=car)
plt.show()


#2. Regression on one variable 
#(a) Regression on one variable for negative correlation
X=car[['highwaympg']]
Y=car[['horsepower']]
reg=linear_model.LinearRegression()
reg.fit(X,Y)
print(reg.coef_)
sns.regplot(X,Y)
plt.show()

#(b) Regression on one variable for positive correlation
X=car[['wheelbase']]
Y=car[['carlength']]
reg=linear_model.LinearRegression()
reg.fit(X,Y)
print(reg.coef_)
sns.regplot(X,Y)
#plt.show()

#(c) Regression on one variable with no correlation
X=car[['stroke']]
Y=car[['price']]
reg=linear_model.LinearRegression()
reg.fit(X,Y)
print(reg.coef_)
sns.regplot(X,Y)
plt.show()



#3. Regression on multiple variables
X=car[['horsepower','curbweight']]
Y=car[['price']]
reg=linear_model.LinearRegression()
reg.fit(X,Y)
print(reg.coef_)

# complete credit to the internet for the below code
df2 = pd.DataFrame(car,columns=['horsepower','curbweight','price'])
import statsmodels.formula.api as smf
model = smf.ols(formula='price ~ horsepower + curbweight', data=df2)
results_formula = model.fit()
results_formula.params


## Prepare the data for Visualization

x_surf, y_surf = np.meshgrid(np.linspace(df2.horsepower.min(), df2.horsepower.max(), 100),np.linspace(df2.curbweight.min(), df2.curbweight.max(), 100))
onlyX = pd.DataFrame({'horsepower': x_surf.ravel(), 'curbweight': y_surf.ravel()})
fittedY=results_formula.predict(exog=onlyX)



## convert the predicted result in an array
fittedY=np.array(fittedY)




# Visualize the Data for Multiple Linear Regression

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df2['horsepower'],df2['curbweight'],df2['price'],c='red', marker='o', alpha=0.5)
ax.plot_surface(x_surf,y_surf,fittedY.reshape(x_surf.shape), color='b', alpha=0.3)
ax.set_xlabel('Horsepower')
ax.set_ylabel('Curbweight')
ax.set_zlabel('Price')
plt.show()