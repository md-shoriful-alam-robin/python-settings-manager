# Write code to open a file named mydata.txt in read mode.
# and find
# wheather it contains the word live.


file= open("certificate.txt", "r")
dataOfFile= file.read()

dataOfFile= dataOfFile.lower()

if "live" in dataOfFile:
  print("Yes Live Word is Present in the File")
else:
  print("No")



