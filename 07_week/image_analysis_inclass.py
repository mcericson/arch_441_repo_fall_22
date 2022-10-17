#mark ericson
#10/3/2022
#This program generates geometry from images

import rhinoscriptsyntax as rs
import System.Drawing.Bitmap as Bitmap
from capture_view import capture_view
from box_tools import center_cube
from box_tools import center_box
file_path  = "web_mountains_small.jpg"



def assign_material_color(object, color):
    rs.AddMaterialToObject(object)
    index = rs.ObjectMaterialIndex(object)
    rs.MaterialColor(index, color)

def image_to_circle(file_path, resolution):
    rs.EnableRedraw(False)
    img = Bitmap.FromFile(file_path)
    
    width = img.Width
    height = img.Height
    
    print (width, height)
    
    w_step = int(width/resolution)
    h_step = int(height/resolution)
    for i in range(0, width, w_step):
        x = i
        for j in range(0, height, h_step):
            y = j
            r, g, b, a = img.GetPixel(x, y)
            location = (x, y, 0)
            circle = rs.AddCircle(location, b/20 + .01)
            color = rs.CreateColor(r, g, b, a)
            rs.ObjectColor(circle, color)

def image_to_line(file_path, resolution):
    rs.EnableRedraw(False)
    img = Bitmap.FromFile(file_path)
    
    width = img.Width
    height = img.Height
    
    print (width, height)
    
    w_step = int(width/resolution)
    h_step = int(height/resolution)
    for i in range(0, width, w_step):
        x = i
        for j in range(0, height, h_step):
            y = j
            r, g, b, a = img.GetPixel(x, y)
            location_1 = (x, y, 0)
            location_2 = (r/20, g/20, b/20)
            line = rs.AddLine(location_1, location_2)
            color = rs.CreateColor(r, g, b, a)
            rs.ObjectColor(line, color)

def image_to_cube(file_path, resolution):
    rs.EnableRedraw(False)
    img = Bitmap.FromFile(file_path)
    
    width = img.Width
    height = img.Height
    
    print (width, height)
    
    w_step = int(width/resolution)
    h_step = int(height/resolution)
    for i in range(0, width, w_step):
        x = i
        for j in range(0, height, h_step):
            y = j
            r, g, b, a = img.GetPixel(x, y)
            location = (x, y, 0)
            cube = center_box(location, r/10 + .01, g/10 + .01, b/10 + .01)
            color = rs.CreateColor(r, g, b, a)
            assign_material_color(cube, color)
            rs.ObjectColor(cube, color)

image_to_cube(file_path, 50)
capture_view(2, "mountain_test", "mountain_test")