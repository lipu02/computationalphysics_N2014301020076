# **The Final Homework**



## *Abstract*
    Based on Alpha Centauri, the C star of which is the nearest star to our sun, we construct a three-star system.
    The model includes three stars of comparable masses, and a planet of negligible mass.
    We investigate the three body problem, using the Euler-Cromer method. 
    Besides, we study the motion of a pseudo planet in this three-star system.
    Also, we generalize the model to cover arbitrary masses of these stars, and arbitrary orbits.
    We use Python to design the programs, which can realize the purpose of this assignment. 
    This article deals with the ideas for these problems, the programs ,and the results.

---

## *Introduction*
 - The motion of celestial objects has always aroused great curiosity in fields like astronomy and astrophysics. It is worthwhile to study a three-star system, which has a chaotic behavior so that it cannot be solved analytically.
 - There are many dramatic phenomenon in the study of planetary motion in a three-star system. Now consider a hypothetical, ideal celestial system consisting of star A, star B, star C, and a planet, which gravity can be ignored compare with that of three stars. All experience only the gravitation produced by the others. A few of the properties for different star masses and orbits are investigated here.

---

## *Body*
### 1. Requirement
 - Construct a three-star system;
 - Specify the situation for Alpha Centauri;
 - Add a planet to this system;
 - Investigate the motion of all four objects;
 - Allow the masses of these stars and their orbits to be adjustable;
 - Plot their trajectories in the mass center frame for arbitrary time;
 - Study the behavior of their motion.


### 2. Ideas
 - We take the average distance between earth and sun, namely 1 AU as the unit of length, and year as the unit of time.
 - We set the initial condition, including position and velocity according to observational or experimental data for the special case of Alpha Centauri. Then we imagine a pseudo earth placed at somewhere in this system.
    1. Semi-major axis of the second star: `a_s=17.57`;
    2. Semi-major axis of the third star: `a_t=15000`;
    3. Semi-major axis of the planet: `a_p=1`(according to the orbit of earth);
    4. Eccentricity of the second star: `e_s=0.5179`;
    5. Eccentricity of the third star: `e_t=0`(still unknown from presenting data, some postulate it as a circle, so we take it as zero);
    6. Eccentricity of the planet: `e_p=0.017`(according to the orbit of earth);
    7. Mass of planet: `m_p=1`, mass of sun as mass unit for the three stars: `m_u=333333.3`;
    8. Mass times of the first star in sun mass: `Sttimes=1.10`;
    9. Mass times of the second star in sun mass: `Ndtimes=0.907`;
    10. Mass times of the third star in sun mass: `Rdtimes=0.123`;
 - Then we list out the equations of motion in the center of mass frame according to the Newton Second law: <br>![](http://latex.codecogs.com/gif.latex?%5C%5C%5Cfrac%7Bd%5E%7B2%7D%5Cvec%7Br%7D_%7BF%7D%7D%7Bdt%5E%7B2%7D%7D%3D-%5Cfrac%7BGM_%7BS%7D%7D%7Br_%7BFS%7D%5E%7B3%7D%7D%5Cvec%7Br%7D_%7BFS%7D-%5Cfrac%7BGM_%7BT%7D%7D%7Br_%7BFT%7D%5E%7B3%7D%7D%5Cvec%7Br%7D_%7BFT%7D%20%5C%5C%5Cfrac%7Bd%5E%7B2%7D%5Cvec%7Br%7D_%7BS%7D%7D%7Bdt%5E%7B2%7D%7D%3D-%5Cfrac%7BGM_%7BF%7D%7D%7Br_%7BSF%7D%5E%7B3%7D%7D%5Cvec%7Br%7D_%7BSF%7D-%5Cfrac%7BGM_%7BT%7D%7D%7Br_%7BST%7D%5E%7B3%7D%7D%5Cvec%7Br%7D_%7BST%7D%20%5C%5C%5Cfrac%7Bd%5E%7B2%7D%5Cvec%7Br%7D_%7BT%7D%7D%7Bdt%5E%7B2%7D%7D%3D-%5Cfrac%7BGM_%7BF%7D%7D%7Br_%7BTF%7D%5E%7B3%7D%7D%5Cvec%7Br%7D_%7BTF%7D-%5Cfrac%7BGM_%7BS%7D%7D%7Br_%7BTS%7D%5E%7B3%7D%7D%5Cvec%7Br%7D_%7BTS%7D%20%5C%5C%5Cfrac%7Bd%5E%7B2%7D%5Cvec%7Br%7D_%7BP%7D%7D%7Bdt%5E%7B2%7D%7D%3D-%5Cfrac%7BGM_%7BF%7D%7D%7Br_%7BPF%7D%5E%7B3%7D%7D%5Cvec%7Br%7D_%7BPF%7D-%5Cfrac%7BGM_%7BS%7D%7D%7Br_%7BPS%7D%5E%7B3%7D%7D%5Cvec%7Br%7D_%7BPS%7D-%5Cfrac%7BGM_%7BT%7D%7D%7Br_%7BPT%7D%5E%7B3%7D%7D%5Cvec%7Br%7D_%7BPT%7D)
 - We give these objects, that is, the second and third star, and the planet, some proper initial conditions including position and velocity according to their semi-major axis and eccentricities. Besides, we set the initial position of the first planet as origin, and the line between the initial position of the first and second star as positive x-axis. Also, we suppose the planet moves in the plane formed by the three stars, and the initial position of the third star is on the negative x-axis.
 - Furthermore, we assign the first star a speed to keep the mass center of this system still.
 - On top of that, we compile the program and input parameter, namely the masses and the orbits of three stars, then we run the program to see the trajectory of these objects.


### 3. Programs
 - [Assignment.py](https://github.com/lipu02/computationalphysics_N2014301020076/blob/master/Final%20Homework/Program.py)


### 4. Results
 - We run the program, and yield the trajectories of these three body problems for several disparate cases in a plane and in 3D, also in local (specify for the first and second stars) and global: 
    1. We suppose a pseudo earth around the first star, set `a_p=1`: <br> ![Assignment-1.png](https://github.com/lipu02/computationalphysics_N2014301020076/blob/master/Final%20Homework/Assignment-1.png) <br> ![Assignment-2.png](https://github.com/lipu02/computationalphysics_N2014301020076/blob/master/Final%20Homework/Assignment-2.png) <br> ![Assignment-3.png](https://github.com/lipu02/computationalphysics_N2014301020076/blob/master/Final%20Homework/Assignment-3.png) <br> ![Assignment-4.png](https://github.com/lipu02/computationalphysics_N2014301020076/blob/master/Final%20Homework/Assignment-4.png)
    2. We suppose a pseudo earth around the second star, set `a_p=17`: <br> ![Assignment-5.png](https://github.com/lipu02/computationalphysics_N2014301020076/blob/master/Final%20Homework/Assignment-5.png) <br> ![Assignment-6.png](https://github.com/lipu02/computationalphysics_N2014301020076/blob/master/Final%20Homework/Assignment-6.png)
    3. We suppose a pseudo earth between the first and the second star, set `a_p=9.2`: <br> ![Assignment-7.png](https://github.com/lipu02/computationalphysics_N2014301020076/blob/master/Final%20Homework/Assignment-7.png) <br> ![Assignment-8.png](https://github.com/lipu02/computationalphysics_N2014301020076/blob/master/Final%20Homework/Assignment-8.png) <br> ![Assignment-9.png](https://github.com/lipu02/computationalphysics_N2014301020076/blob/master/Final%20Homework/Assignment-9.png) <br> ![Assignment-10.png](https://github.com/lipu02/computationalphysics_N2014301020076/blob/master/Final%20Homework/Assignment-10.png)
    4. We suppose a pseudo earth between the second and the third star, set `a_p=8000`: <br> ![Assignment-11.png](https://github.com/lipu02/computationalphysics_N2014301020076/blob/master/Final%20Homework/Assignment-11.png) <br> ![Assignment-12.png](https://github.com/lipu02/computationalphysics_N2014301020076/blob/master/Final%20Homework/Assignment-12.png)
 - Note that for a pseudo earth in Alpha Centauri, if it located as near to one of stars as earth near to sun, it would be relatively stable, rotate around its main star with some sorts of precession. Nevertheless, if unfortunately located between two stars, its trajectory would be apparently chaotic and soon be thrown out of the system. Even if it does survive for approximately 10 million years, it is still too transient for life to evolve, like that in *The Three-Body Problem*.
 - Now we consider a imaginary three star system, in which the three stars are really closed to each other, like that could be infer from *The Three-Body Problem*, and add a pseudo earth to it to study their motions.
 - We set `a_s=20`, `a_t=50`, `a_p=200`, and `e_s=e_t=0`, to investigate how different sets of masses can influence the evolution of this system.
    1. We set `Sttimes=Ndtimes=Rdtimes=1`: <br> ![Assignment-13.png](https://github.com/lipu02/computationalphysics_N2014301020076/blob/master/Final%20Homework/Assignment-13.png) <br> ![Assignment-14.png](https://github.com/lipu02/computationalphysics_N2014301020076/blob/master/Final%20Homework/Assignment-14.png)
    2. We set `Sttimes=1.2`, `Ndtimes=0.9`, and `Rdtimes=1`: <br> ![Assignment-15.png](https://github.com/lipu02/computationalphysics_N2014301020076/blob/master/Final%20Homework/Assignment-15.png) <br> ![Assignment-16.png](https://github.com/lipu02/computationalphysics_N2014301020076/blob/master/Final%20Homework/Assignment-16.png)
    3. We set `Sttimes=0.8`, `Ndtimes=1.1`, and `Rdtimes=1`: <br> ![Assignment-17.png](https://github.com/lipu02/computationalphysics_N2014301020076/blob/master/Final%20Homework/Assignment-17.png) <br> ![Assignment-18.png](https://github.com/lipu02/computationalphysics_N2014301020076/blob/master/Final%20Homework/Assignment-18.png)
    4. We set `Sttimes=0.9`, `Ndtimes=0.8`, and `Rdtimes=1`: <br> ![Assignment-19.png](https://github.com/lipu02/computationalphysics_N2014301020076/blob/master/Final%20Homework/Assignment-19.png) <br> ![Assignment-20.png](https://github.com/lipu02/computationalphysics_N2014301020076/blob/master/Final%20Homework/Assignment-20.png)
    5. We set `Sttimes=1.5`, `Ndtimes=0.3`, and `Rdtimes=1`: <br> ![Assignment-21.png](https://github.com/lipu02/computationalphysics_N2014301020076/blob/master/Final%20Homework/Assignment-21.png) <br> ![Assignment-22.png](https://github.com/lipu02/computationalphysics_N2014301020076/blob/master/Final%20Homework/Assignment-22.png)
    6. We set `Sttimes=1`, `Ndtimes=0.3`, and `Rdtimes=1.5`: <br> ![Assignment-23.png](https://github.com/lipu02/computationalphysics_N2014301020076/blob/master/Final%20Homework/Assignment-23.png) <br> ![Assignment-24.png](https://github.com/lipu02/computationalphysics_N2014301020076/blob/master/Final%20Homework/Assignment-24.png)
 
---

## *Conclusion*
 - As we can see from these graphs, in a three-star system, the planet exhibits a chaotic motion. And it is not long before the planet struck one of the star, which is the plot is exhibit as fly away to infinity far, but actually means the destroy of the planet. As a result, a planet cannot stably exist in a three star system, so the pseudo three body civilization located at Alpha Centauri mentioned in the well selling hard science fiction *The Three-Body Problem* actually could not evolve into a such highly civilized civilization. However, given proper initial conditions, it might be possible for some significant phenomenon such as 'Regular Era', 'Chaotic Era', 'Three stars in a line', 'There stars in the sky', and even 'No sun nearby'.
 - Since three body system is a chaotic system, if we be more meticulous, that is, we take in account the gravity of the planet, though it is extremely small compare with that of the stars, we would still witness dramatic changes in the trajectories, since the extremely sensitive property of this chaotic system.
 - When one of the star is far away from the others, the two neighbor stars would rotate around each other, and they move as a whole in the rotation around the further star, also the further star rotate around them, forming a quasi-two-star system. If the planet is near that two stars, it would exhibits chaotic behavior, just as we have demonstrated in [Ex12](https://github.com/2013301020135/computationalphysics_N2013301020135/blob/master/Chapter-4/Exercise-12/Homework%2012.md), the planet would soon be throw away due to these two star's gravity or even collide with one of them. And if the planet rotates around the lonely star, it would almost rotates around this star regularly, almost forming a stable subsystem, even allows for the probability of the evolution of an intellectual creature.
 - In addition, for the case of Alpha Centauri which are of great interest, due to star C's relatively small mass, the motion of these three stars are relatively stable, i.e., the two neighbor larger star rotate around each other with precession, while the further smaller star rotate around these two with an extremely long period, forming a quasi-two-star system in a whole.
 - But this system would be an inferno for a planet, such as earth, its trajectory is obviously chaotic, which means the creatures on it, if ever exists, must suffer irregular climate condition, such as extremely high and low temperature. To be worse, due to its chaotic movement, it would soon be thrown out of this system or even collide with one of these stars.
     
---

## *Acknowledgment*
   Some pictures and the data for Alpha Centauri are from baidu. Some comparison are made between our results and the phenomenon described in the hard science fiction *The Three-Body Problem* written by Cixin Liu.



