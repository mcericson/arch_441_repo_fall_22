#mark ericson
#RGB cube 10/26/22

import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino
import System
def set_rendered_view():
    views = rs.ViewNames()
    
    for view in views:
        rs.ViewDisplayMode(view,'Rendered')
        rs.ShowGrid(view,show=False)
        rs.ShowGridAxes(view,show=False)
        rs.ShowWorldAxes(view,show=False)

def set_axon_view(rotate_right, rotate_up, view_name):
    rs.ViewProjection(mode=1)
    rs.RotateView(view_name, 0, angle=float(rotate_right))
    rs.RotateView(view_name, 3, angle=float(rotate_up))
    rs.ZoomExtents()

def save_obj(Objects,FileName,NewFolder):


    #This function exports an obj file of whatever geometry is placed in to the objects position.
    #Mark Ericson 3.19.21

    rs.SelectObjects(Objects)
    
    folder = System.Environment.SpecialFolder.Desktop
    path = System.Environment.GetFolderPath(folder)
    #convert foldername and file name sto string
    FName = str(NewFolder)
    File = str(FileName)
    #combine foldername and desktop path
    Dir = System.IO.Path.Combine(path,FName)
    NFolder = System.IO.Directory.CreateDirectory(Dir)
    Dir = System.IO.Path.Combine(Dir,FileName +".obj")
    cmd = "_-Export " + Dir + " _Enter PolygonDensity=1 _Enter"
    rs.Command(cmd)

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
    source = source_max - source_min
    target = target_max - target_min
    value_less = value - source_min
    
    new_value = (target * value_less / source) + target_min
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
    
    r = clamp(remap(x, min, max, 0, 200), 0, 200)
    g = clamp(remap(y, min, max, 0, 200), 0, 200)
    b = clamp(remap(z, min, max, 0, 200), 0, 200)
    
    return r, g, b
def cull_with_sphere(point_list, sphere_center, sphere_radius):
    radius = float(sphere_radius)
    new_list =[]
    for i in point_list:
        distance = rs.Distance(sphere_center, i)
        if distance >= sphere_radius:
            new_list.append(i)
    point_list[:]
    return new_list


def rgb_cube(x_num, y_num, z_num, space):
    points = cubic_grid(x_num, y_num, z_num, space)
    min = 0
    max = x_num
    center_x = float(x_num/2.0)
    center_y = float(y_num/2.0)
    center_z = float(z_num/2.0)
    unit_part = -space/2
    new_points_1 = cull_with_sphere(points, (0+unit_part,0+unit_part,0+unit_part), float(x_num/2))
    new_points_2 = cull_with_sphere(new_points_1, (x_num+unit_part, y_num+unit_part, 0+unit_part), float(x_num/2))
    new_points_3 = cull_with_sphere(new_points_2, (x_num+unit_part, 0+unit_part, 0+unit_part), float(x_num/2))
    new_points_4 = cull_with_sphere(new_points_3, (0+unit_part, y_num+unit_part, 0+unit_part), float(x_num/2))
    for i in new_points_4:
        color = point_to_rgb(i, min, max)
        cube = center_cube(i, float(space/2.0))
        assign_material_color(cube, color)


def create_parallel_view(name, size):
    size_x, size_y = size
    view = Rhino.Display.DefinedViewportProjection.Top
    dimensions = System.Drawing.Rectangle(20,20,size_x,size_y)
    sc.doc.Views.Add(name, view, dimensions,True)


def main():
    rs.EnableRedraw(False)
    create_parallel_view("axo_cube", (2000, 2000))
    rgb_cube(20, 20, 20, 1)
    set_axon_view(45, 120, "axo_cube")
    set_rendered_view()
    command = "Zoom Factor 0.75"
    rs.Command(command)


main()