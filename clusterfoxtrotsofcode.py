import random
import math
import time
import string
#Raised to...code
def power(x,n):
    
    if n == 0:
        return 1
    else:
        return x*power(x,n-1)

#Factorial code
def fact(x):
    
    if x == 0:
        return 1
    else:
        return x*fact(x-1)
#Random numbers between limit
def gen(lim):
    
    l=[]
    if lim==0:
        return 1
    else:
        l.append(random.randint(1,100))
        
        return l , gen(lim-1)

#Check for T/t
def str_count(string):
    
    count=0
    l1=string.split()
    for i in l1:
        i.lower()
        if i == "t":
            count += 1
    print("Count:", count)
#Sum of series 1+1/2-1/3+1/4-1/5......1/n

def ssum(x):
    
    if x==1:
        return 1
    if x%2==0 :
        return(1/x) + ssum(x-1)
    else:
        return-(1/x) + ssum(x-1)

#String separated by hyphens
def hyphen_split(string):
    
    new_str=""
    ask= input("Enter string separated by hypens, Dumbo:")
    l=ask.split("-")
    l.sort()
    
    for i in l:
        new_str= new_str + "-" + i
        
    return new_str.lstrip("-")

#Space split code
def split():
    
    new_str=""
    ask= input("Enter string:")
    l=ask.split(" ")
    l.sort()
    
    for i in l:
        new_str= new_str + "-" + i
            
    return new_str.lstrip("-")
#STACK implementation
def push(push_val):
    stack.append(push_val)
    print(stack)
def pop(n):
    stack.pop()
    if stack==[]:
        print("List is empty.")
    else:
        print("Deleted Element:", stack.pop())
def display(n):
    for i in range(len(stack)-1,-1,-1):
        print(stack(i))
    

        
    

