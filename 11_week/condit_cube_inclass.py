import rhinoscriptsyntax as rs



def cubic_grid(x_num, y_num, z_num,space ):
    points = []
    for i in range(0, x_num, space):
        x = i
        for j in range(0, y_num, space):
            y = j
            for p in range(0, z_num, space):
                z = p
                point = (x,y,z)
                points.append(point)
    return points
    
def center_cube(center, radius):
    cx, cy, cz = center
    
    #lower 4 points
    p1 = (cx - radius, cy - radius, cz - radius)
    p2 = (cx + radius, cy - radius, cz - radius)
    p3 = (cx + radius, cy + radius, cz - radius)
    p4 = (cx - radius, cy + radius, cz - radius)
    
    #upper 4 points
    p5 = (cx - radius, cy - radius, cz + radius)
    p6 = (cx + radius, cy - radius, cz + radius)
    p7 = (cx + radius, cy + radius, cz + radius)
    p8 = (cx - radius, cy + radius, cz + radius)
    
    points = [p1, p2, p3, p4, p5, p6, p7, p8]
    
    cube = rs.AddBox(points)
    return(cube)

def cull_with_sphere(point_list, center, radius):
    new_list = []
    for i in point_list:
        distance = rs.Distance(center, i)
        if distance >= radius:
            new_list.append(i)
    point_list = []
    return new_list

def main():
    rs.EnableRedraw(False)
    space = 1
    cube_dim = 20
    point_list = cubic_grid(cube_dim, cube_dim, cube_dim, space)
    new_list_1 = cull_with_sphere(point_list, (0,0,0), cube_dim/2)
    new_list_2 = cull_with_sphere(new_list_1, (cube_dim, 0 ,0), cube_dim/2)
    new_list_3 = cull_with_sphere(new_list_2, (cube_dim, cube_dim,0), cube_dim/2)
    new_list_4 = cull_with_sphere(new_list_3, (0, cube_dim,0), cube_dim/2)
    new_list_5 = cull_with_sphere(new_list_4, (0,0,cube_dim), cube_dim/2)
    new_list_6 = cull_with_sphere(new_list_5, (cube_dim, 0 ,cube_dim), cube_dim/2)
    new_list_7 = cull_with_sphere(new_list_6, (cube_dim, cube_dim,cube_dim), cube_dim/2)
    new_list_8 = cull_with_sphere(new_list_7, (0, cube_dim,cube_dim), cube_dim/2)
    for i in new_list_8:
        center_cube(i, float(space/2))

main()
