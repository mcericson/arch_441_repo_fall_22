
#equation: (x3, y3, z3)  = (x1, y1, z1) + (x2-x1, y2-y1, z2-z1)*t
#https://mathworld.wolfram.com/Line.html

import rhinoscriptsyntax as rs

def linear_color(color_1, color_2,scalar):
    r1, g1, b1 = color_1
    r2, g2, b2 = color_2
    
    t = float(scalar)
    
    r3 = float(r1 + (r2-r1)*t)
    g3 = float(g1 + (g2-g1)*t)
    b3 = float(b1 + (b2-b1)*t)
    point = rs.AddPoint(r3, g3, b3)
    color = rs.CreateColor(r3, g3, b3)
    return color, point



def main():
    point_1  = (255,100,10)
    point_2 = (10,100,255)

    line = rs.AddLine(point_1, point_2)

    for i in range(11):
        scalar = .1 * i
        print (scalar)
        lin_col = linear_color(point_1, point_2, scalar)
        color = lin_col[0]
        point = lin_col[1]
        rs.ObjectColor(point, color)
        rs.ObjectColor(line, color)


main()

