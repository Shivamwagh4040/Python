print("Demonstration of list")

#data : heterogeneous 
#ordered : yes
#indexed : yes
#mutable : yes
#duplicates : yes

data = [11,21,51,101,21,11]     #duplicates
data1 = [11, 90.80, True, "Hello"]   #heterogeneous

print("Data is Heterogeneous : ",data1)
print("Data is ordered : ",data1)
print("data at index 2 : ",data[2])
print("Data with duplicate elements :",data)

print("list is mutable")
data.append(201)
print("Data after append : ",data)
data.pop()
print("Data after pop : ",data)

