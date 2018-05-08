from splashkit import *
act=0
scene=0
with open('hamlet.txt','r') as file:
    for line in file:
        print(line)
        if 'Now I am alone'.upper() in line.upper():
            print(act,scene)
            break
        if 'Act I'.upper() in line.upper():
            act+=1
            scene=0
        if 'Scene I'.upper() in line.upper():
            scene+=1
        

