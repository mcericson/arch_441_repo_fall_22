
#equation: (x3, y3, z3)  = (x1, y1, z1) + (x2-x1, y2-y1, z2-z1)*t
#https://mathworld.wolfram.com/Line.html

def  linear_color (color_1, color_2,scalar):
    r1, g1, b1 = color_1
    r2, g2, b2 = color_2
    
    t = float(scalar)
    
    r3 = float(r1 + (r2-r1)*t)
    g3 = float(g1 + (g2-g1)*t)
    b3 = float(b1 + (b2-b1)*t)
    return r3, g3, b3
    

color = linear_color((255,10,100), (0,10,255), 1)

def coordinates_to_rgb(coordinates, floor=0.0, ceiling=1.0):
    
    r, g, b = coordinates
    
    max = float(ceiling - floor)
    
    r_mapped = float(max/r * 255)
    g_mapped = float(max/g *255)
    b_mapped = float(max/b *255)
    
    return r_mapped, g_mapped, b_mapped

coord = coordinates_to_rgb((300,10,10))

print (coord)
