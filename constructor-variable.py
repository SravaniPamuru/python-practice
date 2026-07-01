class demo:
    def __init__(self,*a):
        print("constructor with variable number of arguments",*a)

d1=demo()
d2=demo(10)
d3=demo(10,20)
d4=demo(10,20,30)
d5=demo(10,20,30,40,50,60)
        
