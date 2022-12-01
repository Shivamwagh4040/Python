#count the digits in a number

def main():
    num = int(input("Enter a number :"))
    count = 0

    while num != 0:
        num //= 10
        count += 1

    print("Number of Digits :" + str(count))

if __name__ == "__main__":
    main()