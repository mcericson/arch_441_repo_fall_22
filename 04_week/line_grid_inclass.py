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
                rs.AddPoint(point)
    return point_list

def random_color(ceiling):
    red = uniform(0,ceiling)
    green = uniform(0, ceiling)
    blue = uniform(0, ceiling)
    color = rs.CreateColor(red, green, blue)
    return color

def sphere_grid(x_number, y_number, z_number, cell_size):
    #Add a variable sphere to a cubic grid of points.
    points =  cubic_grid(x_number, y_number, z_number, cell_size)
    for i in points:
        radius = uniform(1, 10)
        sphere = rs.AddSphere(i,radius)
        color = random_color(50)
        rs.ObjectColor(sphere, color)

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
            color = random_color(255)
            rs.ObjectColor(line, color)

line_grid(10, 10, 10, 1)



