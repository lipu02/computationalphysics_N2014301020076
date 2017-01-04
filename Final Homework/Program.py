'''
The motion of a planet in a Three-Star system 
2016.06.19.
'''

import numpy as np
from pylab import *
from math import *
import mpl_toolkits.mplot3d

#Information
print 'The motion of a planet in a Three-Star system (especially for Alpha Centauri)'
print 'Designed by Liu Yang 2013301020135 on 2016.06.19.'

#Input the semi-major axises
print 'Input semi-major axis of the second star (17.57) ->',
a_s = float(raw_input())
print 'Input semi-major axis of the third star (15000) ->',
a_t = float(raw_input())
print 'Input semi-major axis of the planet (1) ->',
a_p = float(raw_input())

#Input the eccentricities
print 'Input eccentricity of the second star (0.5179) ->',
e_s = float(raw_input())
print 'Input eccentricity of the third star (0) ->',
e_t = float(raw_input())
print 'Input eccentricity of the planet (0.017) ->',
e_p = float(raw_input())

#Input observation time
print 'Input observation time in unit of year ->',
time = float(raw_input())

#Determine the initial values
def initial(a,e):
    x0=a*(1+e)
    v_y0=2*pi*sqrt((1-e)/(a*(1+e)))
    return [x0,v_y0]

def four_orbits(m_f,m_s,m_t,m_p):
#The third star
    x_t0=-initial(a_t,e_t)[0]
    x_t=[]
    x_t.append(x_t0)
    
    v_tx0=0
    v_tx=[]
    v_tx.append(v_tx0)

    y_t0=0
    y_t=[]
    y_t.append(y_t0)
    
    v_ty0=-initial(a_t,e_t)[1]
    v_ty=[]
    v_ty.append(v_ty0)
#The second star
    x_s0=initial(a_s,e_s)[0]
    x_s=[]
    x_s.append(x_s0)
    
    v_sx0=0
    v_sx=[]
    v_sx.append(v_sx0)

    y_s0=0
    y_s=[]
    y_s.append(y_s0)
    
    v_sy0=initial(a_s,e_s)[1]
    v_sy=[]
    v_sy.append(v_sy0)
#The first star
    x_f0=0
    x_f=[]
    x_f.append(x_f0)
    
    v_fx0=-(m_s*v_sx0+m_t*v_tx0)/m_f
    v_fx=[]
    v_fx.append(v_fx0)

    y_f0=0
    y_f=[]
    y_f.append(y_f0)
    
    v_fy0=-(m_s*v_sy0+m_t*v_ty0)/m_f
    v_fy=[]
    v_fy.append(v_fy0)
#The planet
    x_p0=-initial(a_p,e_p)[0]
    x_p=[]
    x_p.append(x_p0)
    
    v_px0=0
    v_px=[]
    v_px.append(v_px0)

    y_p0=0
    y_p=[]
    y_p.append(y_p0)
    
    v_py0=-initial(a_p,e_p)[1]
    v_py=[]
    v_py.append(v_py0)
#Distance
    r_fs=[]
    r_fs.append(sqrt((x_f0-x_s0)**2+(y_f0-y_s0)**2))
    r_st=[]
    r_st.append(sqrt((x_s0-x_t0)**2+(y_s0-y_t0)**2))
    r_tf=[]
    r_tf.append(sqrt((x_t0-x_f0)**2+(y_t0-y_f0)**2))
    r_fp=[]
    r_fp.append(sqrt((x_f0-x_p0)**2+(y_f0-y_p0)**2))
    r_sp=[]
    r_sp.append(sqrt((x_s0-x_p0)**2+(y_s0-y_p0)**2))
    r_tp=[]
    r_tp.append(sqrt((x_t0-x_p0)**2+(y_t0-y_p0)**2))

    t=[]
    t.append(0)
    dt=0.001
    
    for i in range(int(time/dt)):
#The first star
        v_fx.append(v_fx[i]+dt*(4*pi**2*m_s/m_u*(x_s[i]-x_f[i])/(r_fs[i]**3)+4*pi**2*m_t/m_u*(x_t[i]-x_f[i])/(r_tf[i]**3)))
        x_f.append(x_f[i]+v_fx[i+1]*dt)
        v_fy.append(v_fy[i]+dt*(4*pi**2*m_s/m_u*(y_s[i]-y_f[i])/(r_fs[i]**3)+4*pi**2*m_t/m_u*(y_t[i]-y_f[i])/(r_tf[i]**3)))
        y_f.append(y_f[i]+v_fy[i+1]*dt)
#The second star
        v_sx.append(v_sx[i]+dt*(4*pi**2*m_f/m_u*(x_f[i]-x_s[i])/(r_fs[i]**3)+4*pi**2*m_t/m_u*(x_t[i]-x_s[i])/(r_st[i]**3)))
        x_s.append(x_s[i]+v_sx[i+1]*dt)
        v_sy.append(v_sy[i]+dt*(4*pi**2*m_f/m_u*(y_f[i]-y_s[i])/(r_fs[i]**3)+4*pi**2*m_t/m_u*(y_t[i]-y_s[i])/(r_st[i]**3)))
        y_s.append(y_s[i]+v_sy[i+1]*dt)
#The third star
        v_tx.append(v_tx[i]+dt*(4*pi**2*m_f/m_u*(x_f[i]-x_t[i])/(r_tf[i]**3)+4*pi**2*m_s/m_u*(x_s[i]-x_t[i])/(r_st[i]**3)))
        x_t.append(x_t[i]+v_tx[i+1]*dt)
        v_ty.append(v_ty[i]+dt*(4*pi**2*m_f/m_u*(y_f[i]-y_t[i])/(r_tf[i]**3)+4*pi**2*m_s/m_u*(y_s[i]-y_t[i])/(r_st[i]**3)))
        y_t.append(y_t[i]+v_ty[i+1]*dt)
#The planet
        v_px.append(v_px[i]+dt*(4*pi**2*m_f/m_u*(x_f[i]-x_p[i])/(r_fp[i]**3)+4*pi**2*m_s/m_u*(x_s[i]-x_p[i])/(r_sp[i]**3))+4*pi**2*m_t/m_u*(x_t[i]-x_p[i])/(r_tp[i]**3))
        x_p.append(x_p[i]+v_px[i+1]*dt)
        v_py.append(v_py[i]+dt*(4*pi**2*m_f/m_u*(y_f[i]-y_p[i])/(r_fp[i]**3)+4*pi**2*m_s/m_u*(y_s[i]-y_p[i])/(r_sp[i]**3))+4*pi**2*m_t/m_u*(y_t[i]-y_p[i])/(r_tp[i]**3))
        y_p.append(y_p[i]+v_py[i+1]*dt)

        r_fs.append(sqrt((x_f[i+1]-x_s[i+1])**2+(y_f[i+1]-y_s[i+1])**2))
        r_st.append(sqrt((x_s[i+1]-x_t[i+1])**2+(y_s[i+1]-y_t[i+1])**2))
        r_tf.append(sqrt((x_t[i+1]-x_f[i+1])**2+(y_t[i+1]-y_f[i+1])**2))
        r_fp.append(sqrt((x_f[i+1]-x_p[i+1])**2+(y_f[i+1]-y_p[i+1])**2))
        r_sp.append(sqrt((x_s[i+1]-x_p[i+1])**2+(y_s[i+1]-y_p[i+1])**2))
        r_tp.append(sqrt((x_t[i+1]-x_p[i+1])**2+(y_t[i+1]-y_p[i+1])**2))

        t.append(t[i]+dt)
    return [x_f,y_f,x_s,y_s,x_t,y_t,x_p,y_p,t]


#Input the masses
print 'Input mass times of the first star in unit of sun mass (1.10) ->',
Sttimes = float(raw_input())
print 'Input mass times of the second star in unit of sun mass (0.907) ->',
Ndtimes = float(raw_input())
print 'Input mass times of the third star in unit of sun mass (0.123) ->',
Rdtimes = float(raw_input())

#Define masses
m_p=1.0
m_u=333333.3
m_f=m_u*Sttimes
m_s=m_u*Ndtimes
m_t=m_u*Rdtimes

four=four_orbits(m_f,m_s,m_t,m_p)
x_f=four[0]
y_f=four[1]
x_s=four[2]
y_s=four[3]
x_t=four[4]
y_t=four[5]
x_p=four[6]
y_p=four[7]
t=four[8]

#Plot (local)
figure(figsize=[8,8])
plot(x_f,y_f,color='red')
plot(x_s,y_s,color='yellow')
plot(x_t,y_t,color='blue')
plot(x_p,y_p,color='green')
legend(('First','Second','Third','Planet'),'upper left')
title('three-star system trajectory M_p',fontsize=15)
xlabel('x/AU')
xlim(-50,50)
ylabel('y/AU')
ylim(-50,50)
savefig('Assignment-1.png')
show()

#3D plot (local)
fig = figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_f,y_f,t,color='red')
ax.plot(x_s,y_s,t,color='yellow')
ax.plot(x_t,y_t,t,color='blue')
ax.plot(x_p,y_p,t,color='green')
legend(('Firth','Second','Third','Planet'),'upper left')
ax.set_xlabel('x/Au')
ax.set_ylabel('y/AU')
ax.set_zlabel('t/yr')
ax.set_xlim(-50,50)
ax.set_ylim(-50,50)
savefig('Assignment-2.png')
show()

#Plot (global)
figure(figsize=[8,8])
plot(x_f,y_f,color='red')
plot(x_s,y_s,color='yellow')
plot(x_t,y_t,color='blue')
plot(x_p,y_p,color='green')
legend(('First','Second','Third','Planet'),'upper left')
title('three-star system trajectory M_p',fontsize=15)
xlabel('x/AU')
ylabel('y/AU')
savefig('Assignment-3.png')
show()

#3D plot (global)
fig = figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_f,y_f,t,color='red')
ax.plot(x_s,y_s,t,color='yellow')
ax.plot(x_t,y_t,t,color='blue')
ax.plot(x_p,y_p,t,color='green')
legend(('Firth','Second','Third','Planet'),'upper left')
ax.set_xlabel('x/Au')
ax.set_ylabel('y/AU')
ax.set_zlabel('t/yr')
savefig('Assignment-4.png')
show()
