import pickle
from collections import Counter
file = open('banner.p', 'rb')
image1 = pickle.load(file)
img = ""
for item in image1:
    for par in item:
        img += par[0] * par[1]
    img += "\n"
print(img)
file.close()
