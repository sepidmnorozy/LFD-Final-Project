from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import json

def load_data(x,y):
    # Opening JSON file
    f = open(x, "r")
    # returns JSON object as a dictionary
    data = json.load(f)
    # Iterating through the json list
    embeddings = []
    labels = []
    for article in data:
        embeddings.append(article["vector"])
    # opening JSON file for labels
    label = json.load(open(y, 'r'))
    for article in label:
        labels.append(article["label"])
    return embeddings, labels




# get data

X, Y = load_data("NON_US_res.json", "non-us-labels.json")
split_point = int(0.75 * len(X))
Xtrain = X[:split_point]
Ytrain = Y[:split_point]
Xtest = X[split_point:]
Ytest = Y[split_point:]


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

