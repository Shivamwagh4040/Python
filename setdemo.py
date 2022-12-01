print("Demonstration of set")

#data : heterogeneous 
#ordered : no
#indexed : no
#mutable : yes
#duplicates : no

data = {11,21,51,101,21,11}     #duplicates
data1 = {11, 90.80, True, "Hello"}   #heterogeneous

print("First set data : ",data)
print("Length of data : ",len(data))
print("Data is Heterogeneous : ",data1)
print("Data is unordered : ",data1)
#print("data at index 2 : ",data{2})
print("Data with unique elements :",data)

print("set is mutable")

#insert element in set
data.add(211)
print("data after insertion : ",data)

#remove element
data.remove(211)
print("data after removal : ",data)

data.discard(201)
print("data after discard : ",data)

