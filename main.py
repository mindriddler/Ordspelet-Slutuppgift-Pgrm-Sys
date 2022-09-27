
from base64 import encode


crs = open("words_utf.txt", "r", encoding="UTF-8")
for columns in ( raw.strip().split() for raw in crs ):  
    print (columns[0])
    
    
    
