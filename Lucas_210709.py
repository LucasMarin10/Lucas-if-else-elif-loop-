print("Question 2")
for q in range(1,21):
    print(q)
print("Question 3")
for q in range(1,21):
    if q < 4:
        print(str(q)+" is smaller than 4")
    elif q >= 4 and q < 8:
        print(str(q)+" is bigger than or equal to 4, but smaller than 8")
    elif q >= 8 and q < 12:
        print(str(q)+" is bigger than or equal to 8, but smaller than 12")
    elif q >= 12 and q < 16:
        print(str(q)+" is bigger than or equal to 12, but smaller than 16")
    else:
        print(str(q)+" is bigger than or equal to 16")