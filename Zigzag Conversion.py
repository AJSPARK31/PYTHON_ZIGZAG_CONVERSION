#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Zigzag Conversion
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
s = "PAYPALISHIRING"
numRows = 3
if numRows == 1:
    print(s)
    
    # create the zigzag array
rows = [''] * numRows
currRow = 0
goingDown = False
    
for c in s:
    rows[currRow] += c
    if currRow == 0 or currRow == numRows - 1:
        goingDown = not goingDown
    currRow += 1 if goingDown else -1
    
    # concatenate the characters in each row
print(''.join(rows))


# In[ ]:




