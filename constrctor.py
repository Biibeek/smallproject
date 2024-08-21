class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print("constructor was called!!!")
        

p1=Point(10,20)
print(p1.x)