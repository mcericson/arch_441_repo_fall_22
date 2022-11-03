import keyboard
import rhinoscriptsyntax as rs
from scriptcontext import escape_test

def add_sphere():
    center = rs.GetPoint()
    radius = rs.Distance((0,0,0), center)
    rs.AddSphere(center, radius)


while True:
    escape_test(True)
    if keyboard.is_pressed('j'):
        add_sphere()
    else:
        print('waiting for instructions')