import rhinoscriptsyntax as rs
from scriptcontext import escape_test


def cursor_sphere():
    #draw a circle centered on a point with a 
    #radius equal to the distance from the origin to the center of the circle
    center = (0,0,0)
    point_1 = rs.GetPoint("Please pick a point.")
    radius = rs.Distance(center, point_1)
    rs.AddSphere(point_1, radius)

while True:
    escape_test()
    cursor_sphere()