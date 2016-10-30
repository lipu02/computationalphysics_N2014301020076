import math
import matplotlib.pyplot as plt      
g=9.8 
dt=0.04
#adjust theta to keep it in range of [-pi,+pi]
def adjust(x):
    while x>math.pi:
        x=x-2*math.pi
    while x<-math.pi:
        x=x+2*math.pi
    return x
#2-order Runge-Kutta method
def EC(omega0,theta0,q,l,FD,omegaD,T):
    motion=[[]for i in range(3)]
    motion[0].append(omega0)
    motion[1].append(theta0)
    motion[2].append(0)
    while motion[2][-1]<=T:
        motion[0].append(motion[0][-1]+(-g*math.sin(motion[1][-1])/l-q*motion[0][-1]+FD*math.sin(omegaD*motion[2][-1]))*dt)
        motion[1].append(motion[1][-1]+motion[0][-1]*dt)
        motion[2].append(motion[2][-1]+dt)
    return motion#omega,theta,t



#Figure.1: p.60,fig3.6
omega0,theta0,q,l,omegaD,T=0,0.2,0.5,9.8,0.66,60
d1=EC(omega0,theta0,q,l,0,omegaD,T)
d2=EC(omega0,theta0,q,l,0.5,omegaD,T)
d3=EC(omega0,theta0,q,l,1.2,omegaD,T)
plt.subplot(3,2,1)#
plt.plot(d1[2],d1[1],linestyle='-',linewidth=1.0,label='1')
plt.text(40,0.15,r'$F_D=0$')
plt.title(r'Fig1.1 $\theta$ versus time with different $F_D$')
plt.xlim(0,T)
plt.subplot(3,2,3)#
plt.plot(d2[2],d2[1],linestyle='-',linewidth=1.0)
plt.text(40,0.5,r'$F_D=0.5$')
plt.xlim(0,T)
plt.ylabel(r'$\theta$(radius)',fontsize=15)
plt.subplot(3,2,5)#
plt.plot(d3[2],d3[1],linestyle='-',linewidth=1.0)
plt.text(40,-2,r'$F_D=1.2$')
plt.xlim(0,T)
plt.xlabel('time(seconds)',fontsize=15)
plt.subplot(3,2,2)#
plt.plot(d1[2],d1[0],linestyle='-',linewidth=1.0)
plt.text(40,0.05,r'$F_D=0$')
plt.title(r'Fig.1.2 $\omega$ versus time with different $F_D$')
plt.xlim(0,T)
plt.subplot(3,2,4)#
plt.plot(d2[2],d2[0],linestyle='-',linewidth=1.0)
plt.text(40,0.5,r'$F_D=0.5$')
plt.xlim(0,T)
plt.ylabel(r'$\omega$(radius/second)',fontsize=15)
plt.subplot(3,2,6)#
plt.plot(d3[2],d3[0],linestyle='-',linewidth=1.0)
plt.text(40,1.0,r'$F_D=1.2$')
plt.xlim(0,T)
plt.xlabel('time(seconds)',fontsize=15)
plt.show()
#fig.1.3
plt.subplot(2,1,1)
plt.plot(d3[2],map(adjust,d3[1]),linestyle='-',linewidth=1.0)
plt.text(40,1.0,'adjusted'+'\n$F_D=1.2$')
plt.title(r'Fig.1.3 $\theta$ versus time')
plt.xlim(0,T)
plt.ylabel(r'$\theta$(radius)',fontsize=15)
plt.subplot(2,1,2)
plt.plot(d3[2],d3[1],linestyle='-',linewidth=1.0)
plt.text(40,-2,'unadjusted'+'\n$F_D=1.2$')
plt.xlim(0,T)
plt.xlabel('time(seconds)',fontsize=15)
plt.ylabel(r'$\theta$(radius)',fontsize=15)
plt.show()

#fig.2phase-space plot
d2=EC(omega0,theta0,q,l,0.5,omegaD,500)
d3=EC(omega0,theta0,q,l,1.2,omegaD,500)
plt.subplot(1,2,1)#
plt.plot(map(adjust,d2[1]),d2[0],linestyle='-')
plt.title(r'Fig.2.1 $\omega$ versus $\theta$')
plt.text(0.5,0.6,r'$F_D=0.5$')
plt.xlabel(r'$\theta$(radius)')
plt.ylabel(r'$\omega$(radius/second)')
plt.subplot(1,2,2)#
plt.plot(map(adjust,d3[1]),d3[0],linestyle='-')
plt.title(r'Fig.2.2 $\omega$ versus $\theta$')
plt.text(2,1.4,r'$F_D=1.2$')
plt.xlabel(r'$\theta$(radius)')
plt.ylabel(r'$\omega$(radius/second)')
plt.show()



