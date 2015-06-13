import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm
import pickle

digits = datasets.load_digits()

print(digits.data)

print(digits.target)

print(digits.images[0])
print(digits.images[1])


clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(digits.data[:-1], digits.target[:-1])
clf.predict(digits.data[-1])
print(digits.images[-1])

s = pickle.dumps(clf)
clf2 = pickle.loads(s)
clf2.predict(digits.data[-1])




