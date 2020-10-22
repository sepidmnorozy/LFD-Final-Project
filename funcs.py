import json


def separate_US_embeddings(input_file_address):
    # find the path for US articles
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
        for article in data["articles"]:
            if article["newspaper"] == "The Washington Post" or article["newspaper"] == "New York Times":
                us_articles_path.append(article["path"])
    all = open(input_file_address, "r")
    data = json.load(all)
    US = []
    non_US = []
    for article in data:
        if article["path"] in us_articles_path:
            US.append(article)
        else:
            non_US.append(article)
    with open("US_res.json", "w") as outfile:
        json.dump(US, outfile)
    with open("NON_US_res.json", "w") as outfile:
        json.dump(non_US, outfile)

if __name__ == '__main__':
    separate_US_embeddings("res.json")
