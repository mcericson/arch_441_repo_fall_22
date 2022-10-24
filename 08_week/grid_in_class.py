import rhinoscriptsyntax as rs
rs.EnableRedraw(False)




def cubic_grid(x_num, y_num, z_num, space, start_point):
    points = []
    x_start, y_start, z_start = start_point
    
    for i in range(x_start, x_num+x_start, space):
        x = i
        for j in range(y_start, y_num+y_start, space):
            y = j
            for p in range(z_start, z_num+z_start, space):
                z = p
                point = (x, y, z)
                points.append(point)
                rs.AddPoint(point)
    return points
    
cubic_grid(10, 10, 20, 1, (10,1,10))
#for i in range(0, 10 , 1):
#    x = i
#    for j in range(0, 10, 1):
#        y = j
#        for p in range(0, 10, 1):
#            z = p
#            point = (x,y,z)
#            points.append(point)
#            rs.AddPoint(point)
#print len(points)