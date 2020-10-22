# LFD-Final-Project


Before using this repo please notice:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
NEVER use "git add ." for adding new files to the repository, ALWAYS use "git add filename" one by one for the target files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These files should be in your project:
COP_filt3_sub  GoogleNews-vectors-negative300.bin  produce_embeddings.py  README.md  res.json

these two files "produce_embeddings.py  README.md" are already in github repo but the others NO! because they are large and github d$

to run the produce_embeddings file you should do these steps:
1. add the COP_filt3_sub folder manually and then put the .json data files there (the ones we downloded from TA page)
2. put the google news .bin file in the project folder
3. now you can run the python file and create the res.json

I have also put the res.json on bashupload because of the same reason (large file)
using this command you can access the w2v embeddings for the articles: "wget https://bashupload.com/mU9l8/res.json"

the structure of the res.json file is as following:
[{"path":article path, "vector":300 dimension vector}, ...]



the things we need in the future:
1. code to separate the res.json into two files: US_res.json and NON_US_res.json ---> SEPIDEH
2. code to create labels json file for US and NON_US ---> IOANNA
3. code for a function to get a file and return the embedding or labels in form of a list ---> ALEX


TO BE CONTINUED...



