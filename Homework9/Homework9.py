"""
Created on Thu Apr 28 14:22:51 2016
@author: AF
"""

import matplotlib.pyplot as plt
import numpy as np
from visual import *

class billiard_rectangular:
    def __init__(self,x_0,y_0,vx_0,vy_0,N,dt):
        self.x_0 = x_0
        self.y_0 = y_0
        self.vx_0 = vx_0
        self.vy_0 = vy_0
        self.N = N
        self.dt = dt
    
    def motion_calculate(self):
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.t = [0]
        self.x.append(self.x_0)
        self.y.append(self.y_0)
        self.vx.append(self.vx_0)
        self.vy.append(self.vy_0)
        for i in range(1,self.N):
            self.x.append(self.x[i - 1] + self.vx[i - 1]*self.dt)
            self.y.append(self.y[i - 1] + self.vy[i - 1]*self.dt)
            self.vx.append(self.vx[i - 1])
            self.vy.append(self.vy[i - 1])
            if (self.x[i] < -1.0):
                self.x[i],self.y[i] = self.correct('x>-1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i] = - self.vx[i]
            elif(self.x[i] > 1.0):
                self.x[i],self.y[i] = self.correct('x<1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i] = - self.vx[i]
            elif(self.y[i] < -1.0):
                self.x[i],self.y[i] = self.correct('y>-1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vy[i] = -self.vy[i]
            elif(self.y[i] > 1.0):
                self.x[i],self.y[i] = self.correct('y<1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vy[i] = -self.vy[i] 
            else:
                pass
            self.t.append(self.t[i - 1] + self.dt)
        return self.x, self.y
    
    def correct(self,condition,x,y,vx,vy):
        vx_c = vx/100.0
        vy_c = vy/100.0
        while eval(condition):
            x = x + vx_c*self.dt
            y = y + vy_c*self.dt
        return x-vx_c*self.dt,y-vy_c*self.dt
    
    def reflect(self):
        pass
    
    def plot(self):
        plt.figure(figsize = (8,8))
        plt.xlim(-1,1)
        plt.ylim(-1,1)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.plot(self.x,self.y)
        plt.savefig('chapter3_3.31.png',dpi = 144)
        plt.show()
        
    
class billiard_circle(billiard_rectangular):
    def motion_calculate(self):
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.t = [0]
        self.x.append(self.x_0)
        self.y.append(self.y_0)
        self.vx.append(self.vx_0)
        self.vy.append(self.vy_0)
        for i in range(1,self.N):
            self.x.append(self.x[i - 1] + self.vx[i - 1]*self.dt)
            self.y.append(self.y[i - 1] + self.vy[i - 1]*self.dt)
            self.vx.append(self.vx[i - 1])
            self.vy.append(self.vy[i - 1])
            if (np.sqrt( self.x[i]**2+self.y[i]**2 ) > 1.0):
                self.x[i],self.y[i] = self.correct('np.sqrt(x**2+y**2) < 1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i],self.vy[i] = self.reflect(self.x[i],self.y[i],self.vx[i - 1], self.vy[i - 1])
            self.t.append(self.t[i - 1] + self.dt)
        return self.x, self.y
        
    def reflect(self,x,y,vx,vy):
        module = np.sqrt(x**2+y**2)  ### normalization
        x = x/module
        y = y/module
        v = np.sqrt(vx**2+vy**2)
        cos1 = (vx*x+vy*y)/v
        cos2 = (vx*y-vy*x)/v
        vt = -v*cos1
        vc = v*cos2 
        vx_n = vt*x+vc*y
        vy_n = vt*y-vc*x
        return vx_n,vy_n
        
    def plot(self):
        plt.figure(figsize = (8,8))
        plt.xlim(-1,1)
        plt.ylim(-1,1)
        plt.xlabel('x')
        plt.ylabel('y')
        self.plot_boundary()
        plt.plot(self.x,self.y)
        plt.savefig('chapter3_3.31.png',dpi = 144)
        plt.show()
        
    def phase_space_plot(self):
        plt.figure(figsize = (16,8))
        plt.subplot(121)
        plt.xlabel('x')
        plt.ylabel(r'$v_x$')
        plt.scatter(self.x,self.vx, s=1)
        plt.subplot(122)
        plt.xlabel('y')
        plt.ylabel(r'$v_x$')
        plt.scatter(self.y,self.vx, s=1)
        plt.savefig('chapter3_3.31_phase.png', dpi= 144)
        plt.show()
    
    def phase_plot(self):
        plt.figure(figsize = (8,8))
        record_x = []
        record_vx = []
        for i in range(len(self.x)):
            if (abs(self.y[i] - 0)<0.001):
                record_vx.append(self.vx[i])
                record_x.append(self.x[i])
        plt.xlabel('x')
        plt.ylabel(r'$v_x$')
        plt.scatter(record_x,record_vx,s=1)
        plt.savefig('chapter3_3.31_phasey=0.png', dpi= 144)
        plt.show()
                
        
    def plot_boundary(self):
        theta = 0
        x = []
        y = []
        while theta < 2*np.pi:
            x.append(np.cos(theta))
            y.append(np.sin(theta))
            theta+= 0.01
        plt.plot(x,y)

    def Vplot(self):
        floor = box (pos=(0,0,0), length=4, height=0.3, width=4, material = materials.wood)
        ball = sphere (pos = (self.y_0,0.2,self.x_0),radius = 0.05, material = materials.marble)
        p = paths.circle(pos=(0,0,0),radius = 0.5)
        squ = shapes.rectangle(pos = (0.6,0,0),width = 0.1,height = 0.5)
        extrusion(pos=p, shape=squ, color=color.yellow)
        t = 0
        i = 0
        ball.trail = curve(color = color.white)
        while i < len(self.vx):
            rate(50)
            ball.velocity = vector(self.vy[i],0,self.vx[i])
            ball.pos = ball.pos + ball.velocity*self.dt
            ball.trail.append(pos = ball.pos)
            t = t + self.dt
            i+= 1
        
class billiard_ellipse(billiard_circle):   ### x^2/3+y^2/2 = 1
    def motion_calculate(self):
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.t = [0]
        self.x.append(self.x_0)
        self.y.append(self.y_0)
        self.vx.append(self.vx_0)
        self.vy.append(self.vy_0)
        for i in range(1,self.N):
            self.x.append(self.x[i - 1] + self.vx[i - 1]*self.dt)
            self.y.append(self.y[i - 1] + self.vy[i - 1]*self.dt)
            self.vx.append(self.vx[i - 1])
            self.vy.append(self.vy[i - 1])
            if (self.x[i]**2/3+self.y[i]**2/2 > 1.0):
                self.x[i],self.y[i] = self.correct('x**2/3+y**2/2 < 1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i],self.vy[i] = self.reflect((2./3)*self.x[i],self.y[i],self.vx[i - 1], self.vy[i - 1])
            self.t.append(self.t[i - 1] + self.dt)
        return self.x, self.y       
     
    def plot(self):
        plt.figure(figsize = (8,6))
        plt.xlim(-2,2)
        plt.ylim(-1.5,1.5)
        plt.xlabel('x')
        plt.ylabel('y')
        self.plot_boundary()
        plt.plot(self.x,self.y)
        plt.savefig('chapter3_3.31.png',dpi = 144)
        plt.show()
        
    def plot_boundary(self):
        theta = 0
        x = []
        y = []
        while theta < 2*np.pi:
            x.append(np.sqrt(3)*np.cos(theta))
            y.append(np.sqrt(2)*np.sin(theta))
            theta+= 0.01
        plt.title(r'Elliptical stadium - $\frac{x^2}{3}+\frac{y^2}{2} = 1$')
        plt.plot(x,y)

    def Vplot(self):
        floor = box (pos=(0,0,0), length=4, height=0.3, width=4, material = materials.wood)
        ball = sphere (pos = (self.y_0,0.2,self.x_0),radius = 0.05, material = materials.marble)
        p = paths.ellipse(pos=(0,0,0),width = 2*np.sqrt(2),height=2*np.sqrt(3))
        squ = shapes.rectangle(pos = (0,0,0),width = 0.1,height = 0.5)
        extrusion(pos=p, shape=squ, color=color.yellow)
        t = 0
        i = 0
        ball.trail = curve(color = color.white)
        while i < len(self.vx):
            rate(50)
            ball.velocity = vector(self.vy[i],0,self.vx[i])
            ball.pos = ball.pos + ball.velocity*self.dt
            ball.trail.append(pos = ball.pos)
            t = t + self.dt
            i+= 1
        
class billiard_innercircle(billiard_circle):
    def motion_calculate(self):
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.t = [0]
        self.x.append(self.x_0)
        self.y.append(self.y_0)
        self.vx.append(self.vx_0)
        self.vy.append(self.vy_0)
        for i in range(1,self.N):
            self.x.append(self.x[i - 1] + self.vx[i - 1]*self.dt)
            self.y.append(self.y[i - 1] + self.vy[i - 1]*self.dt)
            self.vx.append(self.vx[i - 1])
            self.vy.append(self.vy[i - 1])
            if (self.x[i] < -1.0):
                self.x[i],self.y[i] = self.correct('x>-1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i] = - self.vx[i]
            elif(self.x[i] > 1.0):
                self.x[i],self.y[i] = self.correct('x<1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i] = - self.vx[i]
            elif(self.y[i] < -1.0):
                self.x[i],self.y[i] = self.correct('y>-1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vy[i] = -self.vy[i]
            elif(self.y[i] > 1.0):
                self.x[i],self.y[i] = self.correct('y<1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vy[i] = -self.vy[i] 
            elif(self.x[i]**2+self.y[i]**2<0.01):
                self.x[i],self.y[i] = self.correct('x**2+y**2 > 0.01',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i],self.vy[i] = self.reflect(self.x[i],self.y[i],self.vx[i - 1], self.vy[i - 1])
            self.t.append(self.t[i - 1] + self.dt)
        return self.x, self.y    
               
        
    def plot_boundary(self):
        theta = 0
        x = []
        y = []
        while theta < 2*np.pi:
            x.append(0.1*np.cos(theta))
            y.append(0.1*np.sin(theta))
            theta+= 0.01
        plt.plot(x,y)
        
class billiard_innercircle2(billiard_circle):
    def motion_calculate(self):
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.t = [0]
        self.x.append(self.x_0)
        self.y.append(self.y_0)
        self.vx.append(self.vx_0)
        self.vy.append(self.vy_0)
        for i in range(1,self.N):
            self.x.append(self.x[i - 1] + self.vx[i - 1]*self.dt)
            self.y.append(self.y[i - 1] + self.vy[i - 1]*self.dt)
            self.vx.append(self.vx[i - 1])
            self.vy.append(self.vy[i - 1])
            if (self.x[i] < -1.0):
                self.x[i],self.y[i] = self.correct('x>-1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i] = - self.vx[i]
            elif(self.x[i] > 1.0):
                self.x[i],self.y[i] = self.correct('x<1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i] = - self.vx[i]
            elif(self.y[i] < -1.0):
                self.x[i],self.y[i] = self.correct('y>-1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vy[i] = -self.vy[i]
            elif(self.y[i] > 1.0):
                self.x[i],self.y[i] = self.correct('y<1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vy[i] = -self.vy[i] 
            elif((self.x[i] - 0.05)**2+self.y[i]**2<0.01):
                self.x[i],self.y[i] = self.correct('(x - 0.05)**2+y**2 > 0.01',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i],self.vy[i] = self.reflect(self.x[i]-0.05,self.y[i],self.vx[i - 1], self.vy[i - 1])
            self.t.append(self.t[i - 1] + self.dt)
        return self.x, self.y    
               
        
    def plot_boundary(self):
        theta = 0
        x = []
        y = []
        plt.title(r'$(x-0.05)^2+y^2 = 0.01$')
        while theta < 2*np.pi:
            x.append(0.1*np.cos(theta)+0.05)
            y.append(0.1*np.sin(theta))
            theta+= 0.01
        plt.plot(x,y)    
    
A = billiard_ellipse(0.5,0.5,0.47,0.323,5000,0.1)
A.motion_calculate()
#A.plot()
#A.phase_plot()
A.Vplot()
