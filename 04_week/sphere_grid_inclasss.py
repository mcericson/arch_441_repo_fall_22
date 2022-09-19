#mark ericson 
#9/12/2022
#This program creates a cubic grid

import rhinoscriptsyntax as rs
from random import uniform
from random import randint


#functions
def cubic_grid(x_number, y_number, z_number, cell_size):
    #stop Rhino from redrawing the window after each loop
    rs.EnableRedraw(False)
    #create an empty list to store the point values in
    point_list = []
    
    #creat the x values
    for i in range(0, x_number,cell_size):
        x = i
        #create the y values
        for j in range(0, y_number, cell_size):
            y = j
            #creat the z values
            for p in range(0, z_number, cell_size):
                z = p
                #create a tuple to store the x, y, z cooridinates
                point = (x,y,z)
                #append the tuple to the list
                point_list.append(point)
                #Add a point to the document
                rs.AddPoint(point)
    return(point_list)
    
def create_random_color(r_max, g_max, b_max):
    #us the random.uniform to create a color 
    red = uniform(0,r_max)
    green = uniform(0,g_max)
    blue = uniform(0,b_max)
    return red, green, blue

def add_material_object(object, material):
        #add material to objects.  Color only works in shaded mode.
        # You must create and add a material for it appear in render mode
        rs.AddMaterialToObject(object)
        mat_index = rs.ObjectMaterialIndex(object)
        rs.MaterialColor(mat_index,material)

def sphere_grid(x_value, y_value, z_value, cell_value):
    #call the cubic grid funtion to create a grid
    points = cubic_grid(x_value, y_value,z_value, cell_value)
    #creat a loop that places a random colored sphere
    #on each point generatted by the cubic_grid function.
    for i in points:
        radius = uniform(1,5)
        red, green, blue = create_random_color(255, 255, 255)
        color = rs.CreateColor(red, green, blue)
        sphere = rs.AddSphere(i,radius)
        rs.ObjectColor(sphere, color)
    print (points)

def line_grid(x_value, y_value, z_value, cell_value):
    points = cubic_grid(x_value, y_value,z_value, cell_value)
    max_index = len(points) - 1
    for i in points:
        radius = uniform(1,5)
        red, green, blue = create_random_color(255, 255, 255)
        color = rs.CreateColor(red, green, blue)
        index_1 = randint(0,max_index)
        index_2 = randint(0,max_index)
        #Rhino will not add a line to a document if it has the same starting point and ending point
        #IF index_1 and index_2 are the same, the starting point and end point will be the same.
        #To prevent this, we us the pass argument so that python simply skips this step.
        
        if index_1 == index_2:
            pass
        else:
            point_1 = points[index_1]
            point_2 = points [index_2]
            path = rs.AddLine((0,0,0), (0,1,1))
            path_2 = rs.AddLine((0,0,0), (1,0,0))
            line = rs.AddLine(point_1, point_2)
            surf = rs.ExtrudeCurve(line, path)
            solid = rs.ExtrudeSurface(surf, path_2)

            
            add_material_object(solid,color)

            #add color to objects
            rs.ObjectColor(line, color)
            rs.ObjectColor(surf, color)
            rs.ObjectColor(solid, color)


##############################################################################
#MAIN program


#This assigns User generated info to a variable to be used in the program
x_value = rs.GetInteger("Please provide the number of units in the x direction.")
y_value = rs.GetInteger("Please provide the number of units in the y direction.")
z_value = rs.GetInteger("Please provide the number of units in the z direction.")
cell_value = rs.GetInteger("Please provide a unit size for the grid.")

#This calls the program that we have created using (3) definitions. 
line_grid(x_value, y_value, z_value, cell_value)




