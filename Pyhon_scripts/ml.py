# Load libraries
from tkinter import Y
from unittest import result
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load dataset
url = "data.csv"
names = ['id', 'tot_familiy', 'age', 'familiy_supp', 'institution', 'last_dossier', 'type_dossier', 'person_type', 'bord_ch', 'civil_state', 'nationality', 'structure', 'motivation', 'occupation', 'last_occupation', 'appresa']
dataset = read_csv(url, names=names)
results = dataset[['last_dossier']].copy()
print(results.head())

print(dataset.groupby('last_dossier').size())

# rmeove useless table
dataset.drop('id', inplace=True, axis=1)
dataset.drop('last_occupation', inplace=True, axis=1)
dataset.drop('appresa', inplace=True, axis=1)
dataset.drop('last_dossier', inplace=True, axis=1)
#dataset.drop('id', inplace=True, axis=1)

print(dataset.head())
'''
print(dataset.head(20))
print(dataset.shape)
print(dataset.describe())
'''

'''
Numero di rimborsi
'''


array = dataset.values
res = results.values
X = array[:,0:]
y = res[:,0]
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)

# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))
# evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = StratifiedKFold(n_splits=6)
	cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
	results.append(cv_results)
	names.append(name)
	print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))