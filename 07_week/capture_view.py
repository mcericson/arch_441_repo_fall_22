#Source: https://github.com/mcneel/rhino-developer-samples/blob/6/rhinopython/SampleViewCaptureToFile.py
#Modified by Mark Ericson to include file/folder directory and scale. 2.18.21

#this function saves the current viewport to the desktop in a specified folder as a png.
#Use scale to scale up or down the viewport size to inccrease/ecrease resolution
#Will overwrite folders and files with same name. 

import Rhino 
import System
import scriptcontext as sc



def capture_view(Scale,FileName,NewFolder):

    view = sc.doc.Views.ActiveView;
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

