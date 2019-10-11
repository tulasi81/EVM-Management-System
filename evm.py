from array import *
voterid=[]
votername=[]
voterage=[]
anand=0
nani=0

def candidate1():
  anand+=1
  c1[]=anand

def candidate2():
  nani+=1
  c2[]=nani

def voter():  
  votername.append(input("Enter voter name:"))
  voterid.append(input("Enter voter id:"))
  voterage.append(input("Enter voter age:"))
  
def castvote():
  n=int(input("Enter your voterid:"))
  for i in range(len(voterid)):
    if(n==voterid[i]):
      print("Candidates in election:")
      print("1.Anand")
      print("2.Nani")
      v=int(input("Cast your vote:"))
      if(v==1):
        print("You have cast your vote to Anand")
        candidate1()
      else:
        print("You have cast your vote to Nani")
        candidate2()

def result():
  print("Total candidates participating in election:2")
  print("1.Anand")
  print("2.Nani")
  print("Total votes to Anand:",len(c1))
  print("Total votes to Nani:",len(c2))
  
 
while(1):
  print("1.Enter voter details:")
  print("2.Cast your vote:")
  print("3.View result:")
  n=int(input("Enter your choice:"))
  if(n==1):
    voter()
  elif(==2n):
  
        
  


  
