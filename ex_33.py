score = input("Enter Score: ")
sc = float(score)
if sc>=1.0 or sc<= 0:
    pass
    print("Score Error")
    exit()
elif sc >= 0.9:
    print("A")
elif sc >= 0.8:
    print("B")
elif sc >= 0.7:
    print("C")
elif sc >= 0.6:
    print("D")
else:
    print("F")
