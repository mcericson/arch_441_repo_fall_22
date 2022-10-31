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



#main
#######################################################

def main():
    #place all code here

#run program
#######################################################
main()