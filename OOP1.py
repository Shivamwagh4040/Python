
class Arithematic:

   def __init__(self,A,B):
      print("Inside init Method")
      self.No1 = A
      self.No2 = B

   def Addition(self):
      Ans = self.No1 + self.No2
      return Ans

   def Substraction(self):
      Ans = self.No1 - self.No2
      return Ans

def main():
   print("Inside Main Method")

   obj = Arithematic(11,10)
   Output = obj.Addition()
   print("Addition is : ",Output)
   Output = obj.Substraction()
   print("Substraction is : ",Output)

   objX = Arithematic(21,20)

if __name__=="__main__":
   print("Inside Starter")
   main()
