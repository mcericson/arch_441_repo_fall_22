#mark ericson
#10/3/2022
#This program generates geometry from images

import rhinoscriptsyntax as rs
import System.Drawing.Bitmap as Bitmap

file_path  = r"C:\Users\ericsonm\OneDrive - Woodbury University\Students_Share\Arch_441_AY22\Arch_441_Class_folder\classes\arch_441_repo_fall_22\06_week\web_mountains_small.jpg"

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

image_to_line(file_path, 100)