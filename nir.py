from visual import *
from visual.graph import *
scene.width = 1024
scene.height = 768
scene.title = "bouncing ball"
scene.forward = (0,-.3,-1)

wall=box(pos=vector(-22,-2,0),size=vector(1.5,8,2),color=vector(0.9,0.7,0.4))
floor=box(pos=vector(-0,-6,0),size=vector(50,0.2,4),color=vector(0.6,0.7,0.4))
ball = sphere(pos=vector(-21.5,2.4,0),velocity=vector(3,10,0),color = color.red, radius = 0.4,make_trail=True,retain=600)

m = 1
g = 9.8
e = 0.8
#gamma = 0.2
dt = 0.01
t=0
while(True):        
    rate(100)     
    ball.pos.x = ball.pos.x + ball.velocity.x*dt    
    ball.pos.y = ball.pos.y + ball.velocity.y*dt
    if(ball.pos.y < floor.pos.y):        
        ball.velocity.y = -e*ball.velocity.y
    else:
        ball.velocity.y = ball.velocity.y - 9.8*dt        
    t = t+dt



