# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 22:39:19 2016
@author: 抽抽
"""

import numpy as np
import matplotlib.pyplot as plt
class State:
    def __init__(self):
        self.ax = [0.0]
        self.ay = [0.0]
        self.vx = [0.0]
        self.vy = [2 * np.pi]
        self.x = [1.0]
        self.y = [0.0]
        self.r = [np.sqrt(self.x[-1]**2 + self.y[-1]**2)]
        pass
    ax = []
    ay = []
    vx = []
    vy = []
    x = []
    y = []
    r = []

Com = State()
Com.__init__()
m1 = State()
r1 = 0.01
m2 = State()
r2 = 0.02
tau = 0.001
t = [0]
beta = [0]
omega = [0]
theta = [0.5 * np.pi]

for i in range(10000):
    # position of center of mass
    Com.r.append(np.sqrt(Com.x[-1] ** 2 + Com.y[-1] ** 2))
    Com.ax.append(-4 * np.pi ** 2 * Com.x[-1] / Com.r[-1] ** 3)
    Com.ay.append(-4 * np.pi ** 2 * Com.y[-1] / Com.r[-1] ** 3)
    Com.vx.append(Com.vx[-1] + tau * Com.ax[-1])
    Com.vy.append(Com.vy[-1] + tau * Com.ay[-1])
    Com.x.append(Com.x[-1] + Com.vx[-1] * tau)
    Com.y.append(Com.y[-1] + Com.vy[-1] * tau)
    beta.append(-3 * 4 * np.pi ** 2 * (Com.x[-1] * np.sin(theta[-1]) - Com.y[-1] * np.cos(theta[-1])) * (Com.x[-1] * np.cos(theta[-1]) + Com.y[-1] * np.sin(theta[-1])))
    omega.append(omega[-1] + tau * beta[-1])
    theta.append(theta[-1] + tau * omega[-1])
    t.append(t[-1] + tau)
    # position of m1 & m2
    m1.x.append(Com.x[-1] + r1 * np.cos(theta[-1]))
    m1.y.append(Com.y[-1] + r1 * np.sin(theta[-1]))
    m2.x.append(Com.x[-1] + r2 * np.cos(theta[-1] + np.pi))
    m2.y.append(Com.y[-1] + r2 * np.sin(theta[-1] + np.pi))

class State_1:
    def __init1__(self):
        self.ax1 = [0.0]
        self.ay1 = [0.0]
        self.vx1 = [0.0]
        self.vy1 = [2 * np.pi]
        self.x1 = [1.0]
        self.y1 = [0.0]
        self.r1 = [np.sqrt(self.x1[-1]**2 + self.y1[-1]**2)]
        pass
    ax1 = []
    ay1 = []
    vx1 = []
    vy1 = []
    x1 = []
    y1 = []
    r1 = []

Com1 = State_1()
Com1.__init1__()
m1_new = State_1()
r1 = 0.01
m2_new = State()
r2 = 0.02
tau = 0.001
t = [0]
beta = [0]
omega = [0]
theta1 = [0.5 * np.pi-0.1]
dtheta = [0]

for i in range(10000):
    # position of center of mass
    Com1.r1.append(np.sqrt(Com1.x1[-1] ** 2 + Com1.y1[-1] ** 2))
    Com1.ax1.append(-4 * np.pi ** 2 * Com1.x1[-1] / Com1.r1[-1] ** 3)
    Com1.ay1.append(-4 * np.pi ** 2 * Com1.y1[-1] / Com1.r1[-1] ** 3)
    Com1.vx1.append(Com1.vx1[-1] + tau * Com1.ax1[-1])
    Com1.vy1.append(Com1.vy1[-1] + tau * Com1.ay1[-1])
    Com1.x1.append(Com1.x1[-1] + Com1.vx1[-1] * tau)
    Com1.y1.append(Com1.y1[-1] + Com1.vy1[-1] * tau)
    beta.append(-3 * 4 * np.pi ** 2 * (Com1.x1[-1] * np.sin(theta1[-1]) - Com1.y1[-1] * np.cos(theta1[-1])) * (Com1.x1[-1] * np.cos(theta1[-1]) + Com1.y1[-1] * np.sin(theta1[-1])))
    omega.append(omega[-1] + tau * beta[-1])
    theta1.append(theta1[-1] + tau * omega[-1])
    t.append(t[-1] + tau)
    dtheta.append((theta[-1]-theta1[-1])*(theta[-1]-theta1[-1]))
    # position of m1 & m2
   # m1_new.x1.append(Com1.x1[-1] + r1 * np.cos(theta1[-1]))
    #m1_new.y1.append(Com1.y1[-1] + r1 * np.sin(theta1[-1]))
    #m2_new.x1.append(Com1.x1[-1] + r2 * np.cos(theta1[-1] + np.pi))
    #m2_new.y1.append(Com1.y1[-1] + r2 * np.sin(theta1[-1] + np.pi))


def plot_COM():
    plt.figure(figsize=(7,7), dpi=80)
    plt.xlim(-1.5,1.5)
    plt.ylim(-1.5,1.5)
    plt.title('Orbit of COM')
    plt.xlabel(r'$x_c /HU$')
    plt.ylabel(r'$y_c /HU$')
    plt.plot(Com.x,Com.y,color="red",  linewidth=1, linestyle="-",label="COM Orbit")
    plt.legend(loc='lower right')
    plt.xticks(np.linspace(-1.5, 1.5, 4, endpoint=True))
    plt.yticks(np.linspace(-1.5, 1.5, 4, endpoint=True))
    plt.savefig('figure_1')
    plt.show()

def plot_omega():
    plt.plot(t,omega)
    plt.title(r'$\omega$ versus time')
    plt.xlabel('time(yr)')
    plt.ylabel(r'$\omega$(radians/yr)')
    #plt.savefig('figure_2')
    plt.show()

def plot_theta():
    plt.plot(t,theta)
    plt.savefig('figure_3')
    plt.show()

def plot_m1m2():
    plt.plot(m1.x,m1.y)
    plt.plot(m2.x,m2.y)
    #plt.savefig('figure_6')
    plt.show()
    
def plot_dtheta():
    plt.plot(t,dtheta)
    plt.title(r'd$\theta$ versus time')
    plt.xlabel('time(yr)')
    plt.ylabel(r'd$\theta$(radians)')
    plt.savefig('figure_circal_dtheta')
    plt.show()
    
    
plot_dtheta()
