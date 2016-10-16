import math
import matplotlib.pyplot as plt
#calculate the trajectory
def Trajectory(v,theta):
    v_x=v * math.cos(theta * math.pi/180)
    v_y=v * math.sin(theta * math.pi/180)
    dt=0.005
    x,y,t=0,0,0
    distance=[[]for i in range(3)]
    distance[0].append(x)
    distance[1].append(y)
    a_x1, a_y1=0,-9.8
    while y>= 0:
        x=x+v_x*dt
        v_x=v_x+a_x1*dt
        y=y+v_y*dt
        v_y=v_y+a_y1*dt
        t=t+dt
        distance[0].append(x/1000)
        distance[1].append(y/1000)
    distance[2].append(t)
    return distance

#plot the figure for various angles
velocity=700
for i in range(7):
    angle=i*5+30
    d=Trajectory(velocity,angle)
    plt.plot(d[0],d[1],linestyle='-',linewidth=1.5,label=angle)
    print angle,d[0][-1],d[2][0]
#generalize the details of the plot    
plt.grid(True,color='k')
plt.title('Trajectory of Cannon Shell with No Air Drag')
plt.xlabel('Horizon Distance x(km)')
plt.ylabel('Vertical Distance y(km)')
plt.text(40,10,"Initial Speed=700m/s")
plt.text(50,9,"No Drag")
plt.xlim(0,60)
plt.ylim(0,20)
plt.legend()
plt.show()
