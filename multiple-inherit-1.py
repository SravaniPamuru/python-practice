class one:
    def hii(self):
        print("hello")
class two:
    def hello(self):
        print("sravani")
class three:
    def welcome(self):
        print("harika")
class four(three,two,one):
    def hey(self):
        print("rupa")
a=four()
a.hey()
a.welcome()
a.hello()
a.hii()
