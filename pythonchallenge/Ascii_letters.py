message = "map" # string they provide
new = ""
import string

for char in message:
    index = string.ascii_lowercase.index(char)
    if index == -1:
        new += char
        continue
    index += 2
    if index >=26:
        index -= 26
    new += string.ascii_lowercase[index]

print(new)
    
        
    
