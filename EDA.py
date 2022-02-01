#basic EDA
import pandas as pd
#import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt

os.chdir("C:/Users/prach/OneDrive/Desktop/Khushi")
#iris = load_iris()
iris = pd.read_csv('Iris.csv')
print(iris.head())
print(iris.describe())
sns.countplot(x='Species', data=iris)
sns.scatterplot('SepalLengthCm','SepalWidthCm', hue='Species',data=iris)
sns.pairplot(iris.drop(['Id'], axis =1),hue='Species',height=2)
#sns.boxenplot()
x=iris.corr(method='pearson')
print(x)
#sns.heatmap(iris.corr_matrix,method='pearson'.drop(['Id'],axis=1).drop(['Id'],axis=0))
sns.heatmap(iris.corr(method='pearson').drop(['Id'],axis=1).drop(['Id'],axis=0))
sns.heatmap(iris.corr(), data = iris)
plt.boxplot('SepalWidthCm', data=iris)
#plt.show()

#cd python3 bin
#python -n pip install seaborn
#pip install seaborn