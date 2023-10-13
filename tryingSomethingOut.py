def pattern_pyramid(x):
    prnt=input("Enter string to be patternized [:p] :")
    for i in range(1,x+1):
        for j in range(i,0,-1):
            print(" "*(j),prnt*(i-j+1))
            
ask=int(input())
pattern_pyramid(ask)
