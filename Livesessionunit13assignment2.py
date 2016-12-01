
myList = [45.4, 44.2, 36.8, 35.1, 39.0, 60.0, 47.4, 41.1, 45.8, 35.6]
print('1. Original list')
print(myList)

print('1a. the 5th element in the list')
print(myList[4])

myList.insert(0,55.2)
print('1b. Append 55.2 to my_list')
print(myList)

print('1c. Remove the 6th element in the list')
del myList[5]
print(myList)

print('1d.Iterate over the list to print data points greater than 45')
for number in myList:	
	if number > 45:
		print(number)
  
import numpy
a = numpy.array([45.4, 44.2, 36.8, 35.1, 39.0, 60.0, 47.4, 41.1, 45.8, 35.6])
print('2a.Import the numpy library using the following command – import numpy')
print('2b.Declare numpy array with the same data points as in my_list using numpy.array()')
print(a)

print('2c.Compute the mean and standard deviation using numpy.mean() and numpy.std() of the above array')
print(numpy.mean(a))
print(numpy.std(a))


print('2d.Use logical referencing to get only those values that are less than 45')
for number in a:	
    if a < 45:  
        print(a)
        break

print('2e.Compute the max and min of the array using numpy.max() and numpy.min()')
print(numpy.max(a))
print(numpy.min(a))

import pandas
print('3a.Import the pandas library – import pandas')
print('3b.Read the IRIS dataset into iris using pandas.read_csv(). Data file – ')
iris = pandas.read_csv('C:/Users/Victor Yim/Downloads/iris.csv')
#from sklearn import datasets
#iris = pandas.DataFrame(datasets.load_iris().data)
print('3c.Using iris.head(), display the head of the dataset')
print(iris.head(10))
print('3d.Use DataFrame.drop() to drop the id column')
iris.drop('Id', axis=1, inplace=True)
print(iris.head(10))


#print('3e.Subset dataframe to create a new data frame that includes only the measurements for the setosa species')
#iris['species'=='Iris-setosa']
#print(iris.head(10))


print('3f.Use DataFrame.describe() to get the summary statistics')
print(iris.describe())
print('3g.Use DataFrame.groupby() to create grouped data frames by Species and compute summary statistics using DataFrame.describe()')
grouped = iris.groupby('Species')
print(grouped.describe())


print('3h.Use DataFrame.boxplot() to plot boxplots by Species')
import matplotlib.pyplot as plt
iris.plot(kind='box', figsize=(12,8))
plt.show()
iris.boxplot(return_type='axes', figsize=(12,8))
plt.show()


import seaborn as sns; sns.set(style='ticks', color_codes=True)
iris = sns.load_dataset('iris')
g = sns.pairplot(iris, hue='species')




