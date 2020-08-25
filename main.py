import sys
sys.path.append('lib')
#from utils import *
import utils

print(dir(utils))
#showName()

class teste():
    a=1
    b=2
    def sum(self):
        self.b=3
        return(a+b)

t=teste()
print(t.sum)

print("hello world")
i=[1,2,3,4]
for aux in i:
    print(aux)

