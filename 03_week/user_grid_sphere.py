import rhinoscriptsyntax as rs
from scriptcontext import escape_test


def cubic_grid(x_number,y_number,z_number,space):
    rs.EnableRedraw(False)
    point_list = []
    for i in range(0, x_number, space):
        x = i
        for j in range(0, y_number, space):
            y = j
            for p in range(0, z_number, space):
                z = p
                rs.AddPoint(x,y,z)


def cursor_sphere():
    #draw a circle centered on a point with a 
    #radius equal to the distance from the origin to the center of the circle
    rs.EnableRedraw(True)
    center = (0,0,0)
    point_1 = rs.GetPoint("Please pick a point.")
    radius = rs.Distance(center, point_1)
    rs.AddSphere(point_1, radius)



cubic_grid(10,10,10,1)

while True:
    escape_test()
    cursor_sphere()