__author__ = 'Administrator'

class Greeter:
    def __init__(self,name):
        self.name = name

    def greet(self,loud=False):
        if loud:
            print('HEELO, %s!' % self.name.upper())
        else:
            print('Hello, %s' % self.name)

g = Greeter('Fred')
g.greet()
g.greet(loud=True)