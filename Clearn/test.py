# coding: utf-8
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

X = [[1,2,3,4,5,6],[2,4,5,8,10,12]]
y = [1,2]
testX = [[3,2,3,6,5,6],[2,4,5,3,7,12]]

cl = SelectKBest(chi2, k=3)
cl.fit(X,y)
newX = cl.transform(X)
newtest = cl.transform(testX)

print newX
print newtest