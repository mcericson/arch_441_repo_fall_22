import rhinoscriptsyntax as rs
from math import sin
from math import cos
from math import radians

def circle(center, radius, point_number):
    point_list = []
    angle_inc = int(360/point_number)
    cx, cy, cz = center
    for i in range(0, 360, angle_inc):

        angle = radians(i)
        x = cos(angle) * radius + cx
        y = sin(angle) * radius + cy
        z = cz
        point = (x, y, z)
        point_list.append(point)
    point_list.append(point_list[0])
    return point_list

points = circle((0,0,0), 10,36)

rs.AddPolyline(points)