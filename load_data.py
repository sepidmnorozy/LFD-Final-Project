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
