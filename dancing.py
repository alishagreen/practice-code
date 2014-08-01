#dancing2 
from time import sleep

print "Dance party!"

a = """  
         0
        \|/
         /\ """

b = """  
         0
        ~|~
         /\ """
c = """  
         0
        -|/
        -\ """
d = """  
          0
        \|-
        /- 
       """
e = """  
         0
        \|/
         |\ """
f = """  
         0
        \|/
        /\ """
g = """  
        \/
        \|/
         0 """

dance_moves = [a, b, c, d, e, f, g, a, b, c, d, e, f, g,] 

for move in dance_moves:
	print move
	sleep(.5)

print "Danced out!" 
