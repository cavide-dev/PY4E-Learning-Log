score = input("Enter Score:")
try :
    s = float(score)
except :
    print("Please enter a numeric number!")
    quit() # If there is an error stop the program.
if s < 0.0 or s > 1.0 :
    print("Error : Score is out of range.")
elif s >= 0.9 :
    print("A")
elif s >= 0.8 :
    print("B")
elif s >= 0.7 :
    print("C")
elif s >= 0.6 :
    print("D")
elif s < 0.6:
    print("F")

# For the test enter 0.85