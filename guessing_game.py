def number_compare(int1, int2):
    if int1 < int2:
        print("Too much!")
    elif int1 > int2:
        print("Too less!")
    else:
        print("Its about time that you got the answer!")
        
import random 
int1= random.randint(0, 50)
for attemptsleft in range(5):
    int2str = input("Please choose ONLY a number between 0 to 50 to play!")
    int2 = int(int2str)
    if(int2==0):
        int1 = 43
    number_compare(int1,int2)
    
