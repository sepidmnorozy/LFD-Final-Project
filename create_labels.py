import numpy, json

us_articles_path = []
file_names = []
for i in range(1, 24):
    name = "COP" + str(i) + ".filt3.sub.json"
    file_names.append(name)
file_names.append("COP6a.filt3.sub.json")
for name in file_names:
    file_address = "./COP.filt3.sub/COP_filt3_sub/" + name
    file = open(file_address, "r")
    data = json.load(file)
    us_labels =[]
    non_us_labels =[]
    for article in data["articles"]:
        temp = {"path":article["path"],"label":""}
        if article["newspaper"] == "The Washington Post" or article["newspaper"] == "New York Times":
            temp["label"] = "left-center"
            us_labels.append(temp)
        else:
            if article["newspaper"] == "Sydney Morning Herald (Australia)" or article[
                "newspaper"] == "The Age (Melbourne, Australia)" or article["newspaper"] == "Mail & Guardian" or \
                    article["newspaper"] == "The Hindu":
                article.update({"political orientation": "left-center"})
            elif article["newspaper"] == "The Australian" or article["newspaper"] == "The Times of India (TOI)" or \
                    article["newspaper"] == "The Times (South Africa)":
                article.update({"political orientation": "right-center"})
            temp["label"] = article["political orientation"]
            non_us_labels.append(temp)
        with open('us-labels.json', 'w') as outfile:
            json.dump(us_labels, outfile)
        with open('non-us-labels.json', 'w') as outfile:
            json.dump(non_us_labels, outfile)