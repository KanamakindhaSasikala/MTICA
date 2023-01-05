class point:
    def __init__( self,x=0,y=0):
        self.x=x
        self.y=y
    def __del__(self):
        class_name=self.__class__.__name__
        print (class_name, "destroyed")

 '''       
output:       
pt1=point()
pt2=pt1

pt3=pt1
print(id(pt1),id(pt2),id(pt3))
2076713303504 2076713303504 2076713303504
del pt1
del pt2
del pt3
point destroyed
pt11=point(5,8)
del pt11
point destroyed
'''
