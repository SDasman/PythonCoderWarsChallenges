filename = "body.txt"
import re
with open(filename) as f:
    matches = re.findall(r'[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', f.read())
print("".join([match[4] for match in matches]))
