#mark ericson 
#9/12/2022
#This program creates a cubic grid

import rhinoscriptsyntax as rs
from random import uniform
from random import randint

def cubic_grid(x_number, y_number, z_number, cell_size):
    rs.EnableRedraw(False)
    point_list = []
    for i in range(0, x_number,cell_size):
        x = i
        for j in range(0, y_number, cell_size):
            y = j
            for p in range(0, z_number, cell_size):
                z = p
                point = (x,y,z)
                point_list.append(point)
                
                rs.AddPoint(point)
    return(point_list)

def sphere_grid(x_value, y_value, z_value, cell_value):
    points = cubic_grid(x_value, y_value,z_value, cell_value)
    for i in points:
        radius = uniform(1,5)
        red = uniform(0,255)
        green = uniform(0,255)
        blue = uniform(0,255)
        color = rs.CreateColor(red, green, blue)
        sphere = rs.AddSphere(i,radius)
        rs.ObjectColor(sphere, color)
    print (points)

def line_grid(x_value, y_value, z_value, cell_value):
    points = cubic_grid(x_value, y_value,z_value, cell_value)
    max_index = len(points) - 1
    for i in points:
        radius = uniform(1,5)
        red = uniform(0,100)
        green = uniform(0,100)
        blue = uniform(0,255)
        color = rs.CreateColor(red, green, blue)
        index_1 = randint(0,max_index)
        index_2 = randint(0,max_index)
        if index_1 == index_2:
            pass
        else:
            point_1 = points[index_1]
            point_2 = points [index_2]
            path = rs.AddLine((0,0,0), (0,1,1))
            path_2 = rs.AddLine((0,0,0), (1,0,0))
            line = rs.AddLine(point_1, point_2)
            surf = rs.ExtrudeCurve(line, path)
            solid = rs.ExtrudeSurface(surf, path_2)
            
            rs.AddMaterialToObject(solid)
            mat_index = rs.ObjectMaterialIndex(solid)
            rs.MaterialColor(mat_index,color)
            rs.ObjectColor(line, color)
            rs.ObjectColor(surf, color)
            rs.ObjectColor(solid, color)





x_value = rs.GetInteger("Please provide the number of units in the x direction.")
y_value = rs.GetInteger("Please provide the number of units in the y direction.")
z_value = rs.GetInteger("Please provide the number of units in the z direction.")
cell_value = rs.GetInteger("Please provide a unit size for the grid.")


line_grid(x_value, y_value, z_value, cell_value)




