import sys
import cs50
def main( ):
    exit=0
    name=input("What is your name? " )

    if name.lower( ) == "brian":
        print("hello, Brian")
    else:
        print("You aren't Brian :(")
        exit=1

    sys.exit(exit)
