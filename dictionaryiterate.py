Batches = {"PPA": 18000, "LB": 16700, "Python": 16500, "Angular": 1500}

print("Data of dictionary : ",Batches)

print("Data traversal using for loop")
for x in Batches:
    print(x)
print("\n_______________________________")

print("Data traversal using for loop")
for x in Batches:
    print(x,Batches[x])
print("\n_______________________________")

print("Data traversal using for loop")
for x in Batches:
    print(x,Batches.get(x))
print("\n_______________________________")

keyBatches = Batches.keys()
print(type(keyBatches))
print(keyBatches)

valueBatches = Batches.values()
print(type(valueBatches))
print(valueBatches)

