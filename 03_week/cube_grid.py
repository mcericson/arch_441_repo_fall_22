import rhinoscriptsyntax as rs
from random import uniform
from random import randint



def cubic_grid(x_number,y_number,z_number,space):
    rs.EnableRedraw(False)
    point_list = []
    for i in range(0, x_number, space):
        x = i
        for j in range(0, y_number, space):
            y = j
            for p in range(0, z_number, space):
                z = p

                point_list.append((x,y,z))
    return(point_list)
     

def line_cube(x_number, y_number, z_number):
    points = cubic_grid(x_number, y_number, z_number,1)
    max_index = len(points) - 1
    for i in points:
        #creat a random radius
        radius = uniform(.5, 3)
        
        #create a random range of colors
        red = uniform(0,255)
        green = uniform(0, 255)
        blue  = uniform(0,255)
        
        #create rhino color
        color = rs.CreateColor(red,green,blue)
        
        #creat a random index
        index = randint(0, max_index)
        
        point_1 = i
        
        #select a point from the list with the random index
        point_2 = points[index]
        
        #draw a line from point_1 to a random point (point_2)
        #only if point_1 does not equal point_2
        if point_1 == point_2:
            pass
        else:
            line = rs.AddLine(point_1, point_2)

            rs.ObjectColor(line, color)
            #create extruded curve
            
            path = rs.AddLine((0,0,0),(0,0,1))
            surf = rs.ExtrudeCurve(line,path)

            rs.ObjectColor(surf, color)

line_cube(10,10,10)

