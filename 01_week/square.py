#import libraries
import rhinoscriptsyntax as rs

#create a program that draws a square beginnig at the origin
def square(side_length):
    #create a point using the rs.Addpoint() function and assign it to a variable
    point_1 = rs.Addpoint(0, 0, 0)
    point_2 = rs.Addpoint(side_length, 0 ,0)
    point_3 = rs.Addpoint(side_length, side_length, 0)
    point_4 = rs.Addpoint(0, side_length, 0)

    #create a polyline with using the 4 point variables as a list []
    square_line = rs.AddPolyline([point_1, point_2, point_3, point_4])

    #send the polyline as the output of the function
    return (square_line)

#call the function
square(100)

