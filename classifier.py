from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.pipeline import Pipeline

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, plot_confusion_matrix
from sklearn.metrics import classification_report


# get data

#Xtrain =
#Ytrain =


# KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=3)
# training
classifier.fit(Xtrain, Ytrain)

# getting the predicted labels for test data from the model
Yguess = classifier.predict(Xtest)

# printing the accuracy_score result for measuring the model performance
print("accuracy_score")
print(accuracy_score(Ytest, Yguess))

print("fscore, recall, precision")
print(classification_report(Ytest, Yguess))

print("confusion_matrix for")
print(confusion_matrix(Ytest, Yguess))
