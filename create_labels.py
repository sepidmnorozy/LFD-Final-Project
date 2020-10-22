import numpy, json

us_articles_path = []
file_names = []
for i in range(1, 24):
    name = "COP" + str(i) + ".filt3.sub.json"
    file_names.append(name)
file_names.append("COP6a.filt3.sub.json")
for name in file_names:
    file_address = "./COP_filt3_sub/" + name
    file = open(file_address, "r")
    data = json.load(file)
    us_labels =[]
    non_us_labels =[]
    for article in data["articles"]:
        temp = {"path":article["path"],"label":""}
        #us
        if article["newspaper"] == "The Washington Post" or article["newspaper"] == "New York Times":
            temp["label"] = "left-center"
            us_labels.append(temp)
        #non-us
        else:
            tmp_label = ""
            if article["newspaper"] == "Sydney Morning Herald (Australia)" or article[
                "newspaper"] == "The Age (Melbourne, Australia)" or article["newspaper"] == "Mail & Guardian" or \
                    article["newspaper"] == "The Hindu":
                tmp_label = "left-center"
            elif article["newspaper"] == "The Australian" or article["newspaper"] == "The Times of India (TOI)" or \
                    article["newspaper"] == "The Times (South Africa)":
                tmp_label = "right-center"
            temp["label"] = tmp_label
            non_us_labels.append(temp)
        with open('us-labels.json', 'w') as outfile:
            json.dump(us_labels, outfile)
        with open('non-us-labels.json', 'w') as outfile:
            json.dump(non_us_labels, outfile)
