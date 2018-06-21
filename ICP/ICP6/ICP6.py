from sklearn import datasets
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
# Implementing Naïve Bayes method using scikit-learn library
from sklearn.model_selection import train_test_split

#Using iris dataset available in the package
irisdatasets=datasets.load_iris()
x=irisdatasets.data
y=irisdatasets.target

#CROSS VALIDATION
#splitting the dataset into two sets(Train and Test)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=0)

model=GaussianNB()
#fitting the model
model.fit(x_train,y_train)
#displaying the score of the model
print(model.score(x_test,y_test))