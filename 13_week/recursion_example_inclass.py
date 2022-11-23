import rhinoscriptsyntax as rs
import scriptcontext as sc
import math


def vector_at_angle(angle, magnitude):
    start_angle = math.radians(angle)
    vec_x = math.cos(start_angle)*magnitude
    vec_y = math.sin(start_angle)*magnitude
    new_vector = (vec_x, vec_y, 0)
    return new_vector


def tree_growth(start_line, min_length, angle):
    end_point = rs.DivideCurve(start_line, 2)[2]
    distance = (rs.CurveLength(start_line))*.5
    vector_right = vector_at_angle(angle, distance)
    vector_left = vector_at_angle(angle + 90, distance)
    point_right = rs.CopyObject(end_point, vector_right)
    point_left = rs.CopyObject(end_point, vector_left)
    right_line = rs.AddLine(end_point, point_right)
    left_line = rs.AddLine(end_point, point_left)
    length = rs.CurveLength(right_line)
    if length > min_length:
        sc.escape_test(True)
        tree_growth(left_line, min_length, angle)
        tree_growth(right_line, min_length, angle)
    

def main():
    start_line = rs.AddLine((0,0,0), (0,50,0))
    tree_growth(start_line, 1, 45)

main()
