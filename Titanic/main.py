#import pandas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#load data
titanic = pd.read_csv('/home/thomas/Code/ds_learning/Python-Lesson/Titanic/Data/train.csv')

#Look at the head of the data
#print(titanic.head())

#Checking the Null values 
print(titanic.isnull().sum())

#Countplot
sns.catplot(x="Sex", hue="Survived", kind="count", data = titanic)
plt.show()