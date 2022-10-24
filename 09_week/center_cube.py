import rhinoscriptsyntax as rs

def center_box(center, width, length, height):
    cx, cy, cz = center
    
    #lower 4 points
    h = height/2
    w = width/2
    l = length/2
    p1 = (cx - w, cy - l, cz - h)
    p2 = (cx + w, cy - l, cz - h)
    p3 = (cx + w, cy + l, cz - h)
    p4 = (cx - w, cy + l, cz - h)
    
    #upper 4 points
    p5 = (cx - w, cy - l, cz + h)
    p6 = (cx + w, cy - l, cz + h)
    p7 = (cx + w, cy + l, cz + h)
    p8 = (cx - w, cy + l, cz + h)
    
    points = [p1, p2, p3, p4, p5, p6, p7, p8]
    
    cube = rs.AddBox(points)
    return(cube,points)


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
    return points


def coordinates_to_color(cooridinates, floor, ceiling):
    max_color = float(255)
    min_color = float(0)
    
    x, y, z = cooridinates
    max_value = ceiling - floor
    r_scalar = x/max_value
    g_scalar = y/max_value
    b_scalar = z/max_value
    
    r = max_color*r_scalar
    g = max_color*g_scalar
    b = max_color*b_scalar
    
    color = rs.CreateColor(r, g, b)
    return color

def assign_material_color(object, color):
    rs.AddMaterialToObject(object)
    index = rs.ObjectMaterialIndex(object)
    rs.MaterialColor(index, color)



def rgb_cube(x_num, y_num,z_num, space, start_point, floor, ceiling):
    rs.EnableRedraw(False)
    points = cubic_grid(x_num, y_num, z_num, space, start_point)
    for i in points:
        cube = center_cube(i,space/2)
        x, y, z = i
        color = coordinates_to_color((x, y, z),floor, ceiling)
        assign_material_color(cube, color)


rgb_cube(20, 20, 20, 1, (0,0,0), 0,20)