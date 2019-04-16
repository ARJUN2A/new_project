#creation of classes
class Point:
    '''Point class represents and manipulates x,y coords.'''
    def __init__(self): #every class can have a special function
        self.x = "hello"
        self.y = 0

#P is object
# No need to pass self 
p = Point()#Instantate an object of type point
q = Point() # Make a second point 

# Accessing object's properties 
# Each object has its own x and y
print(p.x)
print(p.y)
print(q.x)
print(q.y)


