import rhinoscriptsyntax as rs
from random import randint

def grid(x_number, y_number):
    rs.EnableRedraw(False)
    point_list = []
    for i in range(0, x_number, 1):
        x = i
        for j in range(0, y_number, 1):
            y = j
            point = rs.AddPoint(x,y)
            point_list.append(point)
    return(point_list)

def sphere_grid(x_number, y_number):
    points = grid(x_number, y_number)

    for i in points:
        center = (0,0,0) 
        radius = rs.Distance(center, i)
        if radius > 0:
            rs.AddSphere(i,radius)


def line_grid(x_number, y_number, stop):
    points = grid(x_number, y_number)
    max_index = len(points) - 1
    line_count = []
    
    while len(line_count) < stop:
        for i in points:
            red = randint(0,255)
            green = randint(0,100)
            blue = randint(0,100)
            color = rs.CreateColor(red, green, blue)
            index = randint(0, max_index)
            point_2 = points[index]
            dist_points = rs.Distance(i,point_2)
            if dist_points > 0:
                line = rs.AddLine(i,point_2)
                rs.ObjectColor(line, color)
                line_count.append(line)


line_grid(10,10, 10000)