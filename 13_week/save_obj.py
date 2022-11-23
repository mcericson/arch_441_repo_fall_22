import rhinoscriptsyntax as rs
import System

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