from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import KFold
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
kf5 = KFold(n_splits=5, shuffle=False)
rn = range(0,19230)
accuracy_list = []
Xtrain_list = []
Ytrain_list = []
Xtest_list = []
Ytest_list = []
for train_index, test_index in kf5.split(rn):
    print(train_index, test_index)
    Xtrain = []
    Ytrain = []
    Xtest = []
    Ytest = []
    for index in train_index:
        Xtrain.append(X[index])
        Ytrain.append(Y[index])
    Xtrain_list.append(Xtrain)
    Ytrain_list.append(Ytrain)
    for index in test_index:
        Xtest.append(X[index])
        Ytest.append(Y[index])
    Xtest_list.append(Xtest)
    Ytest_list.append(Ytest)


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

