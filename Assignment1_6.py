#check number is positive negative or zero 

def main():

    num = float(input("Enter a number :"))

    if num > 0:
     print("Positive number")

    elif num == 0:
        print("zero")

    else:
        print("Negative number")

if __name__ == "__main__":
    main()