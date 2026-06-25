#Print how many lines are present in notes.txt

import os

try:
  with open("notes.txt", "r") as f:
    listOfLines = f.readlines()   
    print("Output of readLines Function:", listOfLines)
    print("Number of lines in file:", len(listOfLines))
except:
  print("That files does not exist")


#Remaining the file
# 


