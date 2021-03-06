import pandas as pd
import numpy as np

#01
myDF=pd.read_csv('test1.csv')

#2
myDF.iloc[:3]

#3
myDF.drop(["Model"], axis = 1, inplace = False)

#4
del myDF['Model']
print('when running delete command no result is being diplayed we have to call the dataframe again to be able to see the result')
myDF

#5
myDF.drop(index=[1,3,5],inplace=True)
myDF.iloc[:4]

#6
myDF["Range"].mean()

#7
myDF.Type.value_counts().F
myDF['Type'].replace(['F'],'AAA', inplace=True)
myDF.head()

#8
myDF['Cost']=myDF['Cost'].str.replace('$','')
myDF['Cost']=myDF['Cost'].str.replace('[','')
myDF['Cost']=myDF['Cost'].str.replace(']','')
myDF['Cost'].dtypes
myDF.head()
storedf=myDF

#9
myDF['Cost'] = myDF['Cost'].astype(int)
myDF['Cost'].dtypes

#10
myDF['Cost'].mean()
myDF.groupby('Continent').Cost.mean()

#11
#myDF.groupby('Continent').Cost.describe()
myDF.groupby('Continent').agg({'Cost': ['std', 'min', 'max']})

#12
#myDF.groupby('Continent').describe(include=[np.number])
myDF.groupby('Continent').agg(['std', 'min', 'max'],include=[np.number])

#13
myDF.groupby('Continent').mean().plot.bar()

#14
myDF.groupby('Continent').agg({'Continent': ['count']})

#15
myDF['Continent'].value_counts(normalize=True) * 100

#16
myDF['Continent'].unique()
myDF['Continent'].nunique()

#17
myDF['Cost'].value_counts()
#the value_counts() function returns object containing counts of unique values. The resulting object will be in descending order so that the first element is the most frequently-occurring element. Excludes NA values by default.

#18
myDF['Cost'].hist()

#19
myDF['Cost'].hist(bins=50)

#20
myDF['Zip Code'].isnull().sum()
myDF['Type'].isnull().sum()
myDF.isnull().sum()

#21
myDF.dropna(how='any', inplace=False)
myDF

#22
myDF['Type'].value_counts(dropna=False)
#we have 2 missing values

#23
#myDF['Type'].replace(np.nan, "XXX", inplace=True)
myDF['Type'].fillna("XXX", inplace = True) 

#24
myDF.dropna(how='any', inplace=True)
myDF
#NUmber of rows after dropping nan values = 936

#25
myDF.set_index('ID', inplace=True)
myDF.index.name= None
myDF.at[70,'Value']

#26
myDF.index
myDF.columns
myDF.shape
myDF.index.names = ['ID']
myDF.reset_index(inplace = True)
myDF.index
myDF.columns
myDF.shape

#27
des=myDF.describe()
des.at['count','Value']

#28
myDF['Continent'].value_counts().sort_values(ascending=True)
myDF['Continent'].value_counts().sort_index(ascending=True)
myDF['Continent'].value_counts().sort_index(ascending=True).sort_values(ascending=True)

#29
myDF.loc[[1, 3, 5,7], :]
myDF[['Type', 'Continent']].head(7)

#30
myDF.loc[myDF['Type']=='XXX','Value']