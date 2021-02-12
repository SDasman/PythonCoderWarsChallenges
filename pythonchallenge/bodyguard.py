from collections import Counter
filename = "body.txt"
import re
with open(filename) as f:
    text = f.read()
i = 0
msg = ""
while i < len(text)-7:
    phrase = text[i:i+7]
    x = re.search(r'^[A-Z]{3}[a-z][A-Z]{3}', phrase)
    if x:
        print(phrase)
        msg += phrase[3]
        i += 7
        continue
    else:
        continue
    i += 1
print(msg)
