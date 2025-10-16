#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the 
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 63
num_tower= 3
# iterate


for floor in range(num_floors):
  if floor % 21 == 0 :
    x = x + 100
    y = -150
  
  painter.penup()
  painter.goto(x, y)
  
  if floor % 6 > 2: 
    painter.color("blue")
  else:
    painter.color("gray")
  
  y = y + 5

  painter.pendown()
  painter.forward(50)
   

  

  
wn = trtl.Screen()
wn.mainloop()
