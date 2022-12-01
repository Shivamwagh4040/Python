def Add(A,B):
    return A+B

def Sub(A,B):
    return A-B

def Calculator(Name_Of_Operation, Value1, Value2):
    return Name_Of_Operation(Value1,Value2)

Ret = Calculator(Target = Add,Value1 = 10,Value2 = 11)
print("Addition is : ",Ret)

Ret = Calculator(Target = Sub,Value1 = 10,Value2 = 11)
print("Substraction is : ",Ret)