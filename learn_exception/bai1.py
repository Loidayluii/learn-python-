#exception : an event that enterrupts the flow of a program 
#

try : 
    number = int(input("Enter a number : "))
    print(1/number)
except ZeroDivisionError:
    print("you can divided by zero ! Try again")
except Exception:
    print("Something went wrong !")
finally : 
    print("Do some clean up here !") 