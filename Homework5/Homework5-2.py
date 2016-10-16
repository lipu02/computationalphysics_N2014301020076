import math
import matplotlib.pyplot as plt
#calculate the trajectory
def Trajectory(v,theta,B):
    v_x=v * math.cos(theta * math.pi/180)
    v_y=v * math.sin(theta * math.pi/180)
    dt=0.005
    x,y,t=0,0,0
    distance=[[]for i in range(3)]
    distance[0].append(x)
    distance[1].append(y)
    while y>= 0:
        a_x2, a_y2=-B*v*v_x,-9.8-B*v*v_y
        x=x+v_x*dt
        v_x=v_x+a_x2*dt
        y=y+v_y*dt
        v_y=v_y+a_y2*dt
        t=t+dt
        v=(v_x**2+v_y**2)**0.5
        distance[0].append(x/1000)
        distance[1].append(y/1000)
    distance[2].append(t)
    return distance


#plot the figure for various angles
velocity=700
B=4*10**(-5)
for i in range(7):
    angle=i*5+30
    d=Trajectory(velocity,angle,B)
    plt.plot(d[0],d[1],linestyle='-',linewidth=1.0,label=angle)
    print angle,d[0][-1],d[2][0]
#generalize the details of the plot    
plt.grid(True,color='k')
plt.title('Trajectory of Cannon Shell with Air Drag')
plt.xlabel('Horizon Distance x(km)')
plt.ylabel('Vertical Distance y(km)')
plt.text(40,10,"Initial Speed=700m/s")
plt.text(40,9,"B=4*10^(-5)/m")
plt.text(40,8,"With Air Drag")
plt.xlim(0,60)
plt.ylim(0,20)
plt.legend()
plt.show()
