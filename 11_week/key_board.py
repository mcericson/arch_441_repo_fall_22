import keyboard
import rhinoscriptsyntax as rs
from scriptcontext import escape_test
import random

def add_circle():
    center = rs.GetPoint()
    radius = rs.Distance((0,0,0), center)
    circle = rs.AddCircle(center, radius)
    red = random.randrange(0,255,1)
    green = random.randrange(0,255,1)
    blue = random.randrange(0,255,1)
    color = rs.CreateColor(red, green, blue)
    rs.ObjectColor(circle, color)
while True:
    escape_test(True)
    
    if keyboard.is_pressed('j'):
        add_circle()
    else:
        print("waiting")
