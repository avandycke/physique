from math import sin, pi
import matplotlib.animation as animation
import matplotlib.pyplot as plt
#from matplotlib import pyplot, animation
Xmax=10.0
Tmax=10.0
fig = plt.figure()
ax = plt.axes(xlim=(0,Xmax), ylim=(-2,2))
NbEchantillons=100
positionsx=[i*Xmax/NbEchantillons for i in range (NbEchantillons)]
temps=[i*Tmax/NbEchantillons for i in range (NbEchantillons)]
T=2.0
V=1.0
mescourbes=[[sin(2*pi/T*(t-x/V)) for x in positionsx] for t in temps]
courbe, =ax.plot(positionsx, mescourbes[0])
def incrementemps (i):
    courbe.set_ydata(mescourbes [i]) 
    return courbe,
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('propagation d une onde périodique')
line_ani = animation.FuncAnimation(fig,incrementemps, 100, interval=50, blit=False)
plt.show()
