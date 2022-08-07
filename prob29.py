# to check area of the circle using class 
r = int(input("Enter the value of radius:"))

class circle:
    def __init__(self,num):
        self.num = num
    def cir(self):
        print(f"the area of the circle is {3.14*r*r}")
    
sumon = circle(r)
sumon.cir()
