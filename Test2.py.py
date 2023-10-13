import time
import random
d={}
l=["Yes","No","Maybe","Probably","Probably not","I don't know"]
ask=""
k=[]
while ask!="stop":
    ask=input("\nQ: ")
    ask=ask.lower()
    if ask in k:
        print (d[ask])

                
    else:
        k.append(ask)
        a=random.choice(l)
        print(a)
        d[ask]=a
        

