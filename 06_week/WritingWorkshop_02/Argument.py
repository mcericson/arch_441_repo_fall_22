import random
import System
import os



def ArgumentBuilder (Problem, Method, Project):
    
    ind1 = random.randint(0,len(Problem)-1)
    ind2 = random.randint(0,len(Method)-1)
    ind3 = random.randint(0,len(Project)-1)
    
    return (Problem[ind1] + ' ' + Method[ind2]+ ' ' + Project[ind3])

def TitleBuilder (List1,List2):

    ind1 = random.randint(0,len(List1)-1)
    ind2 = random.randint(0,len(List2)-1)

    return (List1[ind1] + ' ' + List2 [ind2])


p = open(r"C:\Users\ericsonm\Dropbox\Woodbury\2021_Sep\Arch_441\WritingWorkshop_02\problem.txt")
m = open(r"C:\Users\ericsonm\OneDrive - Woodbury University\Students_Share\Arch_441\02_Classes\211006\WritingWorkshop_02\method.txt")
pr = open(r"C:\Users\ericsonm\OneDrive - Woodbury University\Students_Share\Arch_441\02_Classes\211006\WritingWorkshop_02\project.txt")

#ta = open("title1.txt")
#tb = open("title2.txt")


problem = p.readlines()

method = m.readlines()
project = pr.readlines()





for i in range(10):
    AG = ArgumentBuilder(problem, method, project)

    print (AG)






