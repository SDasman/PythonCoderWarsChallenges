from collections import Counter
filename = "test.txt"
with open(filename) as f:
    text = f.read()
    important = Counter(char for char in text)
new = {}
for key, value in important.items():
    if value<10:
        new[key] = value
new_msg = ""
for char in text:
    if char in new:
        new_msg += char
print(new_msg)
