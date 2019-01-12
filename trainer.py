#!/usr/bin/python 

# Machine Learning for ShortStocks

from sklearn.neural_network import MLPClassifier
	
X = [[2, 1], [2, 1], [3, 0], [2, 1]]
y = [1, 1, 0, 0]

clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(100, 40, 10, 2), random_state=1)

clf.fit(X, y)

print(clf.predict([[2, 1], [3, 1]]))

            




