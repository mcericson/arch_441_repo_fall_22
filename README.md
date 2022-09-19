#Rhino Python Basics

This is a quick start to programming with python inside Rhino. The links below offer more resources:

##Class Links:

- **Python Programming:** https://woodbury.on.worldcat.org/oclc/44958765
- **Essential Mathematics:** https://developer.rhino3d.com/guides/general/
essential-mathematics/


- **Rhino.Python Guides:** https://developer.
rhino3d.com/guides/rhinopython/

- **RhinoPython Primer:** https://
s3.amazonaws.com/mcneel/misc/docs/en/RhinoPythonPrimerRev3.pdf

- **Google Style Guide:** https://
s3.amazonaws.com/mcneel/misc/docs/en/RhinoPythonPrimerRev3.pdf


## Starting a file in RhinoPython

In order to begin creating geometry in Rhino a library from Rhino must be imported. The easiest to understand library and the one we will begin with is "rhinoscriptsyntax".  To bring this into a python file we use the import function and simplify the name of the library to "rs."It is also import to date, name and explain your program.
```python

#mark ericson 
#9/12/2022
#This program creates a circle

import rhinoscriptsyntax as rs
```
Next we can add geometry to the document by calling a function from the rhinoscriptsyntax library and adding variables. The structure of a function is:

```python
function_name(variable)
```
To call a rhinosriptsyntax funtion we can simply begin by typing "rs." Once we enter the "." afer rs the library should appear a scrollable window.  We can now call the rs.AddCircle() function.

```python
rs.AddCircle(center, radius)
```
A hint will appear in the bottom of the editor that will explain what variables are need and in what format.  In this case we need a plane or center and a radius. The radius is a numerical value, but the center is a set of coordinates stored in data format called a tuple (more on this later).  A tuple is a set of values stored in parantheses: (0, 0, 0). The completed program will look like this:

```python
#mark ericson 
#9/12/2022
#This program creates a circle

import rhinoscriptsyntax as rs

#A program the creates a circle of radius 20 at 0,0,0.
rs.AddCircle((0,0,0), 20)
```
The text that appears after the "#" is a comment. These are notes for the programmer that will be ignored by the computer. Please use these as much as possible to clarify the intent of your code.  We have now mad a very simple program. We can move on to doing something the computer is very good at: repetition.

##Loops

A loop is a fundamental part of writing programs.  It instructs the computer to complete a series of operations a specified number of times or untila condition is reached. To begin we will start with a "for loop". This kind of loop iterates over a specified quantity.  

```python
for i in steps:
    do something(i)
```
This program tells the computer to do something for every i in a set of information called steps. We don't know whats is in steps, and it doesn't matter.  If there are 10 items in steps, the program will iterated over them 10 times.

Another way to work with "for loops" is to specify the number of steps be taken. We can do this with the range function.

```python 
range(start, stop, step)
```

If we add this to our for loop:

```python

for i in range(0, 10 , 1):
    do_something()
```
This program will execute the do_something() function 10 times. To see this more clearly we can replace do_something() with print().  The print function will print whatever we put inside the parantheses.

```python
for i in range(0, 10, 1):
    print(i)
```
If you run this program, it will print:
```terminal
1
2
3
4
5
6
7
8
9
```

The range function started counting at 0 with 1 step between each count and stopped before it hit 10.  If we change the step to 3, we will get something different:
```python
for i in range(0, 10, 3):
    print(i)
```
```terminal
0
3
6
9
```
The range function started counting at 0 with a step of 3 and finished before it hit 10, the stop.

We can now apply this our circle program by adding the circle to the loop:

```python 
import rhinoscriptsyntax as rs

for i in range(1,10, 1):
    rs.AddCircle((0,0,0), i)
```
Importantly, we had to set the start to 1, because we cannot create a circle with radius of 0. The program should now have drawn circles of radius:  1, 2, 3, 4, 5, 6, 7, 8,  and 9 all centered at 0,0,0.

## Nested Loops and Grids

Grids are a fundamental structure used to organize architecture. In order to create a grid we need to use loops. However single loop will only produce a one dimensional array of points:  a line.

```python 
import rhinoscriptsyntax as rs

for i in range(0,10, 1):
    x = i
    rs.AddPoint(x, 0, 0)
```
This program will produce a set of points on the X axis begining at (0,0,0) and ending at (9,0,0.
In order to great a grid we need to add a nother dimension by creating a nested loop:

```python 
for i in range(0, 10, 1):
    x = i
    for j in range(0, 10, 1):
        y = j
        rs.AddPoint(x, y, 0)
```
This program creates a grid of 100 points.  When it runs notice that it draws the entire grid again when each point is added. This is because the window is being refresed or "redrawn" with each pass through the loop to speed up the program we can add one line of code to disable redraw and speed up the execution.

```python
rs.EnableRedraw(False)
```
To create a three-dimensional grid, we simply need to add another nested loop to our program:

```python 
for i in range(0, 10, 1):
    x = i
    for j in range(0, 10, 1):
        y = j
        for p in range(0, 10, 1):
            z = p
            rs.AddPoint(x, y, z)
```
A three dimensional grid should appear with 1000 points. Each nested loop has exponentially increased the total number of points:

- One dimensional loop of length 10 = 10 points
- Two dimensional loop of length 10 = 100 points
- Three dimensional loop of length 10 = 1000 points

## Definitions

In python we can create our own functions called definitions. A definition is a set of operations that have been encapsulated in a single call:

```python
def function_name(variable):
    something = do_something(variable)
    return something
```

The above function is named "function_name" and given space to accept one variable.  The variable is then passed onto the function "do_something" and the information it creates is assigned to the variable "something".  Lastly, the variabel "something" is returned by the funciton so it can be used outside. This is how the function is created.  To call the function in a program one only needs to writ:

```python
fucntion_name(variable)
```
This simplifies the appearance of the code and allows the program to be edited later and updated. For example, if we decided to loop through the do_something function instead:
```python
def function_name(variable):
    for i in range(0, 10, 1):
        something = do_something(variable)
    return something
```
Once we edit the definition, everytime we call this function in the program it will reflect this new change. 

    
