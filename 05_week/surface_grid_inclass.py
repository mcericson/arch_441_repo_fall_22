#mark ericson 
#9/23/2022
#This program creates a cubic grid in which to position a set of randomly colored solids

import rhinoscriptsyntax as rs
from random import uniform
from random import randint

def cubic_grid(x_number, y_number, z_number, cell_size):
    rs.EnableRedraw(False)
    point_list = []
    for i in range(0, x_number, cell_size):
        x = i
        for j in range(0, y_number,cell_size):
            y = j
            for p in range(0, z_number,cell_size):
                z = p
                point = (x,y,z)
                point_list.append(point)
    return point_list

def random_color(floor, ceiling):
    red = uniform(floor,ceiling)
    green = uniform(floor, ceiling)
    blue = uniform(floor, ceiling)
    color = rs.CreateColor(red, green, blue)
    return color

def linear_color(start_color, stop_color, scalar):
    #extract color values from tuple
    red_1, green_1, blue_1 = start_color[0], start_color[1], start_color[2]
    red_2, green_2, blue_2 = stop_color[0], stop_color[1], stop_color[2]
    
    #find differences between color values
    red_diff = red_2 - red_1
    green_diff = green_2 - green_1
    blue_diff = blue_2 - blue_1
    
    #calculate new color
    red_3 = float(red_1 + red_diff*scalar)
    green_3 = float(green_1 + green_diff*scalar)
    blue_3 = float(blue_1 + blue_diff*scalar)
    
    return rs.CreateColor(red_3, green_3, blue_3)

def sphere_grid(x_number, y_number, z_number, cell_size):
    #Add a variable sphere to a cubic grid of points.
    points =  cubic_grid(x_number, y_number, z_number, cell_size)
    for i in points:
        radius = uniform(1, 10)
        sphere = rs.AddSphere(i,radius)
        color = random_color(50)
        rs.ObjectColor(sphere, color)

def solid_from_line(line, height, width):
    
    path_1 = rs.AddLine((0, 0, 0), (0,0 , height))
    surf = rs.ExtrudeCurve(line, path_1)
    path_2 = rs.AddLine((0, 0, 0), (width,0 ,0 ))
    solid = rs.ExtrudeSurface(surf, path_2)
    return solid
    
def assign_material_color(object_id, color):
    rs.AddMaterialToObject(object_id)
    index = rs.ObjectMaterialIndex(object_id)
    rs.MaterialColor(index, color)


#main program
def line_grid(x_number, y_number, z_number, cell_size):
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
            surf = solid_from_line(line, 1,1)
            color = random_color(0,255)
            rs.ObjectColor(surf, color)
            assign_material_color(surf, color)
    curves = rs.ObjectsByType(4, True)
    surfaces = rs.ObjectsByType(8, True)
    
    rs.DeleteObjects(curves)
    rs.DeleteObjects(surfaces)



line_grid(10, 10, 10, 1)



