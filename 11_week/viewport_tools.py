import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino
import System



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
    rs.ZoomExtents()

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

def create_parallel_view(view_name, size, display="Rendered"):
    """Creates a new viewport in top, parallel view.
    view_name:  name of view to be added
    size:  Tuple of X and Y dimensions in pixels of the viewport to be created (x_size, y_size)
    display_mode: Sets the mode of of display.  If None == "Rendered".  
    "Rendered", "Wireframe", "Ghosted", "Shaded", "X-Ray", "Arctic", "Technical", "Artistic", "Pen"
    example:
    create_parallel_view("Axo", (800,800), display_mode="Rendered")
    """
    size_x, size_y = size
    view = Rhino.Display.DefinedViewportProjection.Top
    dimensions = System.Drawing.Rectangle(20,20,size_x,size_y)
    sc.doc.Views.Add(view_name, view, dimensions,True)
    set_display_mode(view_name, display)

def zoom_scale(percentage):
    """
    Zooms the active window by a value
    example:
    zoom_scale(.75)
    """
    rs.EnableRedraw(True)
    command = "Zoom Factor" + " " + str(float(percentage))
    rs.Command(command)
