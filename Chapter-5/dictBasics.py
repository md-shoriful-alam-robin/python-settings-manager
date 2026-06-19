#Dictionary Basics


student= {
  "name": "Aditya",
  "City": "Habiganj",
  "Age": 25,
  "RollNumber": 23
}

print(type(student))
print(student["City"])
student["City"]= "Hyderabad"
student["Country"]= "Germany" #Add item
student.pop("Country") #Remove item

print(student.keys())




