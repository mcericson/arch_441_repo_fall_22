
import rhinoscriptsyntax as rs

def KochCurve(Line,Max):
    
    
    SLine = Line
    
    #rotate line to get perp vector
    Center = rs.DivideCurve(SLine,2)[1]
    RotLine = rs.RotateObject(SLine,Center,90,copy = True)
    End = rs.CurveEndPoint(RotLine)
    Vector = rs.VectorCreate(Center,End)
    VectorU = rs.VectorUnitize(Vector)
    rs.DeleteObject(RotLine)
    
    
    #property to define Max depth of recursion
    Length = rs.CurveLength(Line)
    
    
    DPoints = rs.DivideCurve(SLine, 3, create_points = True)
    Divide2 = rs.DivideCurve(SLine,2,False)
    Midpoint = rs.AddPoint(Divide2[1])
    Distance = (rs.CurveLength(SLine))/3
    
    VectorS = rs.VectorScale(VectorU,Distance)
    
    Point2 = rs.MoveObject(Midpoint,VectorS)
    DPoints.insert(2,Point2)
    Pline = rs.AddPolyline(DPoints)
    Plines = rs.ExplodeCurves(Pline)
    rs.DeleteObject(SLine)
    rs.DeleteObject(Pline)
    
    #set recurcsion depth
    if Length > Max:
        for i in Plines:
            KochCurve(i,Max)
    
#define shape to apply koch curve to
circle = rs.GetObject()
points = rs.DivideCurve(circle,6,True)
rs.DeleteObject(circle)
points.append(points[0])

PLine = rs.AddPolyline(points)
PLines = rs.ExplodeCurves(PLine)
rs.DeleteObject(PLine)

for i in PLines:
    KochCurve(i,2)