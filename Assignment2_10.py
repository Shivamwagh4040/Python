#addition of digits of a number

def main():
    num = int(input("Enter a number :"))
    sum = 0
    i = 0
    for i in num:
        sum = sum + int(i)

    print(sum)

if __name__ == "__main__":
    main()