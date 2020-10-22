import gensim
import regex
import numpy as np
import json


def preprocess(txt):
    res = ''
    if txt is not None and len(txt) > 1:
        punc_list = ["?", "!", ":", ";", ",", ".", "(", ")", "[", "]", "{", "}"]
        for punc in punc_list:
            txt_list = [s.replace(punc, "") for s in txt]
            res = ''.join(txt_list)

    return txt


def get_word2vec(input_text):
    tokens = regex.findall(r'\p{Letter}+', input_text)
    vector = np.zeros(300)
    if len(tokens) > 0:
        for token in tokens:
            if token in wvmodel:
                token_vector = wvmodel[token]
                vector += token_vector
        vector = vector/len(tokens)
    return vector


file_names = []
for i in range(1, 24):
    name = "COP"+str(i)+".filt3.sub.json"
    file_names.append(name)
file_names.append("COP6a.filt3.sub.json")

#file = open("./GoogleNews-vectors-negative300.bin", "rb")
wvmodel = gensim.models.KeyedVectors.load_word2vec_format("/home/s4580427/word2vec/GoogleNews-vectors-negative300.bin", binary=True)

w2v_embeddings = []
article_embedding = {"path": "", "vector": ""}
for name in file_names:
    print(name)
    file_address = "./COP_filt3_sub/"+name
    file = open(file_address, "r")
    data = json.load(file)
    for article in data["articles"]:
        article_embedding["path"] = article["path"]
        text = preprocess(article["headline"]) + preprocess(article["body"])
        article_embedding["vector"] = get_word2vec(text).tolist()
        w2v_embeddings.append(article_embedding)

with open("res.json", "w") as outfile:
    json.dump(w2v_embeddings, outfile)





