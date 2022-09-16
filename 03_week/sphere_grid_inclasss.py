#mark ericson 
#9/12/2022
#This program creates a cubic grid

import rhinoscriptsyntax as rs
from random import uniform

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

x_value = rs.GetInteger("Please provide the number of units in the x direction.")
y_value = rs.GetInteger("Please provide the number of units in the y direction.")
z_value = rs.GetInteger("Please provide the number of units in the z direction.")
cell_value = rs.GetInteger("Please provide a unit size for the grid.")





points = cubic_grid(x_value, y_value,z_value, cell_value)


for i in points:
    radius = uniform(1,5)
    rs.AddSphere(i,radius)
print (points)