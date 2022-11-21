#mark ericson
#RGB cube 10/26/22

import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino
import System
from imp import reload

#user libraries
def capture_view(Scale,FileName,NewFolder):
    
    """
    Captures the active viewport as a .png file
    Scale:  Float value to multiply existing viewport dimensions by
    FileName:  Name of file that you would like to save
    NewFolder:  Name of folder to be created on your desktop

    example:
    capture_view(2.0, "test_drawing", "drawing_folder") 
    """

    view = sc.doc.Views.ActiveView
    if view:
        view_capture = Rhino.Display.ViewCapture()
        view_capture.Width = view.ActiveViewport.Size.Width*Scale
        view_capture.Height = view.ActiveViewport.Size.Height*Scale
        view_capture.ScaleScreenItems = False
        view_capture.DrawAxes = False
        view_capture.DrawGrid = False
        view_capture.DrawGridAxes = False
        view_capture.TransparentBackground = False
        bitmap = view_capture.CaptureToBitmap(view)
        if bitmap:
            #locate the desktop and get path
            folder = System.Environment.SpecialFolder.Desktop
            path = System.Environment.GetFolderPath(folder)
            #convert foldername and file name sto string
            FName = str(NewFolder)
            File = str(FileName)
            #combine foldername and desktop path
            Dir = System.IO.Path.Combine(path,FName)
            #creat path to the new folder
            NFolder = System.IO.Directory.CreateDirectory(Dir)
            Dir = System.IO.Path.Combine(Dir,FileName +".png")
            print (Dir)
            #save the file
            bitmap.Save(Dir, System.Drawing.Imaging.ImageFormat.Png);
            Rhino.Display
    return view

def set_viewports_mode(display_mode="Rendered"):
    """
    sets all viewports display mode
    display_mode: Sets the mode of of display.  If None == "Rendered".  
    "Rendered", "Wireframe", "Ghosted", "Shaded", "X-Ray", "Arctic", "Technical", "Artistic", "Pen"
    set_viewports_mode
    """
    rs.EnableRedraw(True)
    views = rs.ViewNames()
    print(views)
    for view in views:
        rs.ViewDisplayMode(view,display_mode)
        rs.ShowGrid(view,show=False)
        rs.ShowGridAxes(view,show=False)
        rs.ShowWorldAxes(view,show=False)

def set_axon_view(rotate_right, rotate_up, view_name):
    """ 
    sets an axonometric view by rotating the view.
    rotate_right:  Angle in degrees to rotate the right
    rotate_up:  Angle in degrees to rotate the model up
    view_name:  Saved name of view 
    example:
    set_axon_view(45, 120, "Top")

    """
    rs.EnableRedraw(True)
    rs.ViewProjection(mode=1)
    rs.RotateView(None, 0, angle=float(rotate_right))
    rs.RotateView( None, 3, angle=float(rotate_up))
    

def set_display_mode(view_name, display_mode="Rendered"):
    """
    Sets the disaplay mode of a specific viewport
    view_name: name of the view
    display_mode: Sets the mode of of display.  If None == "Rendered".  
    "Rendered", "Wireframe", "Ghosted", "Shaded", "X-Ray", "Arctic", "Technical", "Artistic", "Pen"
    example:
    set_display_mode("Top", display_mode="Wireframe")
        """
    rs.EnableRedraw(True)
    viewport = sc.doc.Views.Find(view_name, False).ActiveViewport
    mode = Rhino.Display.DisplayModeDescription.FindByName("Rendered")
    viewport.DisplayMode = mode

def create_parallel_view(view_name, size):
    """Creates a new viewport in top, parallel view.
    view_name:  name of view to be added
    size:  Tuple of X and Y dimensions in pixels of the viewport to be created (x_size, y_size)
    create_parallel_view("Axo", (800,800), display_mode="Rendered")
    """
    size_x, size_y = size
    view = Rhino.Display.DefinedViewportProjection.Top
    dimensions = System.Drawing.Rectangle(20,20,size_x,size_y)
    sc.doc.Views.Add(view_name, view, dimensions,True)
  

def zoom_scale(zoom_factor, view_name):
    """
    Zooms the active window by a value
    example:
    zoom_scale(.75)
    """
    rs.EnableRedraw(True)
    factor = rs.ViewCameraLens() * float(zoom_factor)
    rs.ViewCameraLens(view_name, factor)


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
        rs.ObjectColor(cube, color)
def clear_file():
    delete = rs.GetString("Would you like to delete all objects?", "No", ["Yes", "No"])
    if delete == "Yes":
        all_objects = rs.AllObjects()
        rs.DeleteObjects(all_objects)
    else:
        pass

__commandname__ = "create_rgb_cube"

# RunCommand is the called when the user enters the command name in Rhino.
# The command name is defined by the filname minus "_cmd.py"
def RunCommand( is_interactive ):
    clear_file()
    rs.EnableRedraw(False)
    cube_dim = rs.GetInteger("Please provide a dimension for the cube", minimum=4, maximum=20)
    rgb_cube(cube_dim, cube_dim, cube_dim, 1)
    rs.EnableRedraw(True)
    view_name = "axo_cube"
    create_parallel_view(view_name, (800, 800))
    set_axon_view(45, 120, view_name)
    rs.ZoomExtents()
    zoom_scale(.75, view_name)
    set_display_mode(view_name, "Rendered")
    animation = rs.GetString("Save animation?", "No", ["Yes", "No"])
    if animation == "Yes":
        file_name = rs.GetString("What is the file name?")
        folder_name = file_name + "_folder"
        resolution = rs.GetInteger("Please provide a scalar for the image", minimum=.5, maximum=10)
        for i in range(360):
            rs.Sleep(1)
            set_axon_view(1, 5, view_name)
            animate_name = file_name + str("%04d"%i)
            #vt.capture_view(resolution, animate_name, folder_name)

RunCommand(True)