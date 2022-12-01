#return addition of factors of a number

def findFactors(num: int)->list:
  factors=[]
  for i in range(1,num+1):
     if num%i==0:
         factors.append(i)
  return factors