
from pylab import *

p.set_wave(100)
x,y = p.capture1('A1', 500,50)
plot(x,y)

p.set_wave(100, 'tria')
x,y = p.capture1('A1', 500,50)
plot(x,y)

show()
