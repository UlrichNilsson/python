score = input("Enter Score: ")
try:
    score=float(score)
except:
    print("Use numeric value")
    quit()
    
if(score>= 0.9):
    print("A")
    quit()
elif(score>= 0.8): 
    print("B")
    quit()
elif(score>= 0.7):
    print("C")
    quit()
elif(score>= 0.6):
    print("D")
    quit()
elif(score< 0.6): 
    print("F")
    quit()
    