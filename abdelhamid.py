import numpy as np
import matplotlib.pyplot as plt
finalTime=20 #Seconds
H=0
velocity=np.zeros(finalTime+1)#Initialize Velocity Array
height=np.zeros(finalTime+1)#Initialize Height Array
g=10 # m/s^2 you may change to 9.81 m/s^2
initialVelocity=100 #Initial Velocity in m/s
# calculate velocity and distance/height at each second
# Time=1; so not appearing in expressions v=u-gt and H=ut-0.5*gt^2
for i in range (0,finalTime+1):
    if i==0:
        velocity[i]=initialVelocity
    else: 
        velocity[i]= velocity[i-1]-g
        deltaH= velocity[i-1]-0.5*g
        H=H+deltaH
        height[i]=H
# initialVelocity=velocity[i]

# initialVelocity=velocity[i]
#print(i, initialVelocity, H)
timePoints=np.linspace(0,finalTime, finalTime+1)
print("velocity", velocity)
print("\n")
print("height", height)

plt.scatter(timePoints, 
velocity, c='r', 
label='data')
plt.plot(timePoints, 
velocity, label='v=u-gt')
plt.xlabel('Time')
plt.ylabel('Velocity ')
plt.title('Fitting primes')
plt.legend()
plt.show()

plt.scatter(velocity, height, c='r', label='data')
plt.plot(velocity, height, label='H=ut-0.5*gt^2')
plt.xlabel('velocity')
plt.ylabel('height')
plt.title('Fitting primes')
plt.legend()
plt.show()