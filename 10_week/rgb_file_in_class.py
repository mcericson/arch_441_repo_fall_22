#student_name
#date
#project_name
#project descriptions

#sources
#######################################################



#imports
#######################################################
import rhinoscriptsyntax as rs



#definitions
#######################################################


def cubic_grid(x_num, y_num, z_num, space):
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
    
def assign_material_color(object, color):
    rs.AddMaterialToObject(object)
    index = rs.ObjectMaterialIndex(object)
    rs.MaterialColor(index, color)

def remap(value, source_min, source_max, target_min, target_max):
   source = float(source_max - source_min)
   target = float(target_max - target_min)
   value_less = float(value - source_min)
   
   new_value = float(target *value_less/source) + target_min
   return new_value

def clamp(value, floor, ceiling):
    if value < floor:
        return floor
    if value > ceiling:
        return ceiling
    else:
        return value

def point_to_rgb(point, min, max):
    
    x, y, z = point 
    
    r = clamp(remap(x, min, max, 0, 255), 0, 255)
    g = clamp(remap(y, min, max, 0, 255), 0, 255)
    b = clamp(remap(z, min, max, 0, 255), 0, 255)
    
    return r, g, b

def rgb_cube(x_num, y_num, z_num, space):
    points = cubic_grid(x_num, y_num, z_num, space)
    min = 0
    max = x_num
    radius = 15
    
    for i in points:
        distance = rs.Distance((0,0,0), i)
        if distance > radius:
            color = point_to_rgb(i, min, max)
            cube = center_cube(i,float(space/2))
            assign_material_color(cube, color)
        else:
            pass
    

#main
#######################################################

def main():
    rs.EnableRedraw(False)
    rgb_cube(20, 20, 20, 1)

#run program
#######################################################
main()