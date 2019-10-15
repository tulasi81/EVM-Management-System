from array import *

voterid=[101,102,103,104,105,106,107,108,109,110]
vname=['a','b','c','d','e','f','g','h','i','j']
vage=[19,22,23,24,26,27,28,29,30,22]
ameer=0
handrew=0
nirup=0

def verify(id):
    yes=0
    no=0
    for i in range(10):
        if(id==voterid[i]):
            yes+=1
        else:
            no+=1
    if(yes==1):
        return 1
    elif(no>1):
        return 2


    

print("***ELECTRONIC VOTING MACHINE MANAGEMENT SYSTEM***")   
while(1):
    print("1.Enter voter details")
    print("2.Cast votes:")
    print("3.View Election result")
    n=(int(input("Enter your choice:")))
    if(n==1):
        for i in range(10):
            print("Votername=",vname[i])
            print("Voterid=",voterid[i])
            print("Voterage=",vage[i])
            print("\n")
    elif(n==2):
        k=0
        l=0
        j=0
        for i in range(10):
            id=int(input("Enter your voter id:"))
            m = verify(id)
            if(m == 1):
                print("Candidates in elections:")
                print("1.Ameer")
                print("2.Handrew")
                print("3.Nirup")
                v=int(input("Cast your vote:"))
                if(v==1):
                    ameer+=1
                elif(v==2):
                    handrew+=1
                elif(v==3):
                    nirup+=1
            else:
                print("You are not eligible to vote:")
    elif(n==3):
        print("Voting results for this election:")
        print("Ameer:",ameer)
        print("Handrew",handrew)
        print("Nirup",nirup)
        
        
                    
                
        
    
    
