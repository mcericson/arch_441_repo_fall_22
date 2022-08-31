import rhinoscriptsyntax as rs

plane = rs.CreatePlane((0,0,0))

for i in range(5,30,5):

    rs.AddCircle(plane, i)
    print (i)
print ("Done")


