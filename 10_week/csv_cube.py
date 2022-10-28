import csv
import rhinoscriptsyntax as rs


#source: https://developer.rhino3d.com/guides/rhinopython/python-csv-file/
#source: https://www.geeksforgeeks.org/reading-csv-files-in-python/


with open('cube.csv', mode = 'r') as file:
    
    csv_file = csv.reader(file)
    points = []
    for line in csv_file:
        
        try:
            x = float(line[0])
            y = float(line[1])
            z = float(line[2])
            point = (x,y,z)
            points.append(point)
            rs.AddPoint(point)
            
        except:
            pass
    rs.AddBox(points)

