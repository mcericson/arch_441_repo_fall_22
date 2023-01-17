#mark ericson
#10/3/2022
#This program generates geometry from images



import rhinoscriptsyntax as rs
import System.Drawing.Bitmap as Bitmap
from capture_view import capture_view
import time

file_path  = "web_mountains_small.jpg"


def assign_material_color(object, color):
    rs.AddMaterialToObject(object)
    index = rs.ObjectMaterialIndex(object)
    rs.MaterialColor(index, color)

def center_cube(center, radius):
    cx, cy, cz = center
    
    #lower 4 points
    p1 = (cx - radius, cy - radius, cz - radius)
    p2 = (cx + radius, cy - radius, cz - radius)
    p3 = (cx + radius, cy + radius, cz - radius)
    p4 = (cx - radius, cy + radius, cz - radius)
    
    #upper 4 points
    p5 = (cx - radius, cy - radius, cz + radius)
    p6 = (cx + radius, cy - radius, cz + radius)
    p7 = (cx + radius, cy + radius, cz + radius)
    p8 = (cx - radius, cy + radius, cz + radius)
    
    points = [p1, p2, p3, p4, p5, p6, p7, p8]
    
    cube = rs.AddBox(points)
    return(cube)
def center_box(center, width, length, height):
    cx, cy, cz = center
    
    #lower 4 points
    h = height/2
    w = width/2
    l = length/2
    p1 = (cx - w, cy - l, cz - h)
    p2 = (cx + w, cy - l, cz - h)
    p3 = (cx + w, cy + l, cz - h)
    p4 = (cx - w, cy + l, cz - h)
    
    #upper 4 points
    p5 = (cx - w, cy - l, cz + h)
    p6 = (cx + w, cy - l, cz + h)
    p7 = (cx + w, cy + l, cz + h)
    p8 = (cx - w, cy + l, cz + h)
    
    points = [p1, p2, p3, p4, p5, p6, p7, p8]
    
    box = rs.AddBox(points)
    return(box)


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
            cube = center_box(location, r/20 + .01, g/20 + .01, b/10 + .01)
            color = rs.CreateColor(r, g, b, a)
            rs.ObjectColor(cube, color)
            assign_material_color(cube, color)

print (time.localtime())
minutes = time.localtime()[4]
seconds = time.localtime()[5]

current_time = str(minutes) + "_" + str(seconds)

image_to_cube(file_path, 50)
