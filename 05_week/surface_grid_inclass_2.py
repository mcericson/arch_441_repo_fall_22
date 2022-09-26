#mark ericson 
#9/12/2022
#This program creates a cubic grid

import rhinoscriptsyntax as rs
from random import uniform
from random import randint

def cubic_grid(x_number, y_number, z_number, cell_size):
    rs.EnableRedraw(False)
    point_list = []
    for i in range(0, x_number, cell_size):
        x = i
        for j in range(0, y_number, cell_size):
            y = j
            for p in range(0, z_number, cell_size):
                z = p
                point = (x,y,z)
                point_list.append(point)
    return point_list

def random_color(ceiling):
    red = uniform(0,ceiling)
    green = uniform(0, ceiling)
    blue = uniform(0, ceiling)
    color = rs.CreateColor(red, green, blue)
    return color


def assign_material_color(object, color):
    rs.AddMaterialToObject(object)
    index = rs.ObjectMaterialIndex(object)
    rs.MaterialColor(index, color)

def solid_from_line(line, height, width):
    path_1 = rs.AddLine((0,0,0), (0, 0, height))
    path_2 = rs.AddLine((0,0,0), (width, width, height))
    surf = rs.ExtrudeCurve(line, path_1)
    solid = rs.ExtrudeSurface(surf, path_2) 
    color = random_color(255)
    assign_material_color(solid, color)
    rs.ObjectColor(line, color)
    rs.ObjectColor(surf, color)
    rs.ObjectColor(solid, color)
    rs.DeleteObject(line)
    rs.DeleteObject(surf)
    
###main program
def line_grid(x_number, y_number, z_number, cell_size, height, width):
    #Add a variable line in a cubic grid of points.
    points =  cubic_grid(x_number, y_number, z_number, cell_size)
    max_index = len(points) - 1 
    for i in points:
        index_1 = randint(0, max_index)
        index_2 = randint(0, max_index)
        point_1 = points[index_1]
        point_2 = points[index_2]
        if point_1 == point_2:
            pass
        else:
           
            line = rs.AddLine(point_1, point_2)
            solid_from_line(line, 1, 1)




line_grid(10, 10, 10, 1, 1, 1)





