from splashkit import *

with open('hamlet.txt','r') as file:
    for line in file:
        print(line)
        delay(10)
