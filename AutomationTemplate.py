from sys import *

def Script_Task(No):
    if((No % 2) == 0):
        print("It is even number")
    else:
        print("It is odd number")

def main():
    print("--------------- Shivam Wagh's Automations ----------------")

    print("Automation script started with name : ",argv[0])

    if(len(argv) != 2):
        print("Error : Insufficient arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("Help : This script is used to perform _____________")
        exit()

    elif((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage : Provide ________ number of arguments as")
        print("First Argument as :__________")
        print("Second Argument as :_________")
        exit()

    else:
        Script_Task(int(argv[1]))

if __name__ == "__main__":
    main()