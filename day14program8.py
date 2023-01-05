##multilevel inheritance:
class A:
    def first_method(self):
        print("Method of class A...")
class B:
    def first_method(self):
        print("Method of class B...")
class C(B,A):
    def third_method(self):
        print("Method of class C...")
        #super().first_method()        
if __name__=='__main__':
    ob=C()
    ob.first_method()
    ob.third_method()
    #C().third_method
'''
output:
================
class C(A,B):
Method of class A...
Method of class C...
class C(B,A):
Method of class B...
Method of class C...
'''
