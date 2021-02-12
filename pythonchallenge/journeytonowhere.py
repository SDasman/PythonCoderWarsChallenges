# We get told: http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=51877
# So when you go to the url it gives you another number to put.

import requests
import re
num = ['12345']
for i in range(0,400):
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + "".join(num)
    r = str(requests.get(url).content)
    print(r)
    num = re.findall('[0-9]+', r)
print(num)

#When you study this you get the answer.
