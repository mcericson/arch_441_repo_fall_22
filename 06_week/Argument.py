import random
import System
import os



def argument_builder(problem, method, project):
    
    ind1 = random.randint(0,len(problem)-1)
    ind2 = random.randint(0,len(method)-1)
    ind3 = random.randint(0,len(project)-1)
    
    return (problem[ind1] + ' ' + method[ind2]+ ' ' + project[ind3])

def title_builder (list_1, list_2):

    ind1 = random.randint(0,len(list_1)-1)
    ind2 = random.randint(0,len(list_2)-1)

    return (list_1[ind1] + ' ' + list_2[ind2])

def thesis_writer(title_1_file, title_2_file, problem_file, method_file, project_file, destination_file, iterations):


    p = open(problem_file)
    m = open(method_file)
    pr = open(project_file)
    
    ta = open(title_1_file)
    tb = open(title_2_file)
    
    title_1 = ta.readlines()
    title_2 = tb.readlines()

    problem = p.readlines()
    method = m.readlines()
    project = pr.readlines()
    
    thesis = open(destination_file, 'w')
    
    thesis_list = []
    for i in range(iterations):
        title = title_builder(title_1, title_2)
        arg = argument_builder(problem, method, project)
        
        print (title)
        print (arg)
        
        thesis_list.append([title, arg])


    
    for i in thesis_list:
        thesis.writelines(i)
        thesis.writelines('\n')

    thesis.close()


thesis_writer('title1.txt', 'title2.txt','problem.txt', 'method.txt', 'project.txt', 'thesis.txt', 200)





