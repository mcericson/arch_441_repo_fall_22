import rhinoscriptsyntax as rs

def square(side_length):
    
    point_1 = (0, 0, 0)
    point_2 = (side_length, 0, 0)
    point_3 = (side_length, side_length, 0)
    point_4 = (0, side_length, 0)
    
    square_line = rs.AddPolyline([point_1, point_2, point_3, point_4, point_1])
    
    return (square_line)

square(100)