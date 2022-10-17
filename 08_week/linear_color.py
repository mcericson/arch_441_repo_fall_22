
#equation: (x3, y3, z3)  = (x1, y1, z1) + (x2-x1, y2-y1, z2-z1)*t
#https://mathworld.wolfram.com/Line.html

import rhinoscriptsyntax as rs

def  linear_color (color_1, color_2,scalar):
    r1, g1, b1 = color_1
    r2, g2, b2 = color_2
    
    t = float(scalar)
    
    r3 = float(r1 + (r2-r1)*t)
    g3 = float(g1 + (g2-g1)*t)
    b3 = float(b1 + (b2-b1)*t)
    return rs.CreateColor(r3, g3, b3)

def grid(x_num, y_num, space):
    points = []
    for i in range(0, x_num, space):
        x = i
        for j in range(0, y_num, space):
            y = j
            point = (x,y)
            points.append(point)
    return points

def linear_color_grid(x_num, y_num, space, color_1, color_2):
    rs.EnableRedraw(False)
    points = grid(x_num, y_num,space)
    length = float(len(points))
    color_inc = float(1.0/length)
    color_scale = 0.0
    for i in points:
        color_scale += color_inc
        point = rs.AddPoint(i)
        color = linear_color(color_1, color_2, color_scale)
        rs.ObjectColor(point, color)

linear_color_grid(100, 100, 1 , (255,10,100), (100,10,255))





