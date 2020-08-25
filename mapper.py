"""mapper.py"""

import sys
import string

for line in sys.stdin:
    line = line.strip()
    
    line = line.translate(str.maketrans(string.punctuation + "“”‘’", " " * (len(string.punctuation) + 4)))
    
    line = line.lower()
    
    words = line.split()
    
    for word in words:
        print (word, 1)
        


