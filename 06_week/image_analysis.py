import rhinoscriptsyntax as rs

import System.Drawing.Bitmap as Bitmap

file_path = r'C:\Users\ericsonm\Dropbox\Woodbury\2023_Jan\Arch_562\web_mountains_small.jpg'

def image_to_line(file_path, resolution):
    rs.EnableRedraw(False)
    img = Bitmap.FromFile(file_path)

    width = img.Width
    height = img.Height

    w_step = width/resolution
    h_step = height/resolution
    
    
    print (width, height)
    lines = []
    for i in rs.fxrange(0, width, w_step):
        x = int(i)
        for j in rs.fxrange(0, height, h_step):
            y = int(j)
            r, g, b, a = img.GetPixel(x,y)
            location_1 = (x, y, 0)
            location_2 = (r, g, b)
            line = rs.AddLine(location_1, location_2)
            color = rs.CreateColor(r, g, b, a)
            rs.ObjectColor(line, color)
            lines.append(line)
    return lines


def image_to_circle(file_path, resolution):
    rs.EnableRedraw(False)
    img = Bitmap.FromFile(file_path)
    #get image width from img object
    width = img.Width
    height = img.Height
    #create a step based on resolution and convert to integer
    #so it will work in the range function
    w_step = int(width/resolution)
    h_step = int(height/resolution)
    
    
    print (width, height)
    
    #create a loop for a 2d grid that covers the dimensions of the image.
    for i in range(0, width, w_step):
        x = i
        for j in range(0, height, h_step):
            y = j
            #get the r,g, b, a values from the img object
            r, g, b, a = img.GetPixel(x,y)
            location = (x, y, r/5)
            circle = rs.AddCircle(location, 2)
            color = rs.CreateColor(r, g, b, a)
            rs.ObjectColor(circle, color)

#call the function
image_to_circle(file_path, 100)