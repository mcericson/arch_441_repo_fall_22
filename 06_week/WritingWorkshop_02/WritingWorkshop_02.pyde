from TitleBuilder import TitleBuilder
from ArgumentBuilder import ArgumentBuilder


Count = 0

              
def setup():
    
    background(255)


def draw():
    
    Problem =  loadStrings("problem.txt")
    Method  =  loadStrings("method.txt")
    Project =  loadStrings("project.txt")
    Title1  =  loadStrings("title1.txt")
    Title2  =  loadStrings("title2.txt")
    
    global Count
    
    Count = Count + 1
    
    title = TitleBuilder(Title1,Title2) + ":  " + TitleBuilder(Title1,Title2)

    
    Argument = ArgumentBuilder(Problem,Method,Project)
    
    
    #print r[0]
    
    print title
    print '_'
    print Argument
    print '_'
    print '_'
    

    
        
    if Count >= 40:
        
    

        noLoop()
  
