import turtle  
while True:
    tt = turtle.Turtle() 
      
    spec_side = int(input("Enter max number of sides:"))
    side_length = 70
      
    for i in range(1,spec_side):
        angle = 420/i
        tt.forward(side_length) 
        tt.right(angle) 

