import rhinoscriptsyntax as rs
import scriptcontext as sc
import math
import random
def tree_growth(min_length, angle, start_line):
    
    start_point = rs.DivideCurve(start_line, 2)[0]
    end_point = rs.DivideCurve(start_line, 2)[2]
    start_angle = math.radians(angle) 
    vec_x = math.cos(start_angle)
    vec_y = math.sin(start_angle)
    vector_1 = (vec_x, vec_y,0)
    vector_2 = (-vec_x, vec_y,0)
    scale = (rs.CurveLength(start_line))*.5
    vector_right = rs.VectorScale(vector_1, scale)
    vector_left = rs.VectorScale(vector_2,  scale)
    point_right = rs.CopyObject(end_point, vector_right)
    point_left =  rs.CopyObject(end_point, vector_left)
    right_line = rs.AddLine(end_point, point_right)
    left_line = rs.AddLine(end_point, point_left)
    length = rs.CurveLength(left_line)
    if length > min_length:
        sc.escape_test(True)
        tree_growth(min_length, angle, left_line)
        tree_growth(min_length, angle, right_line)

    
start_line = rs.AddLine((0,0,0),(0,50,0))
tree_growth(.5, 45, start_line)