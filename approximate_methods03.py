import os
import getpass
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text', usetex=True)


"""
    a simple python script to plot the solutions to the transport equation
"""
    


"""
    parameters for the simulation
"""
method1=1 # 1==triangular
dx=100.
dt=2.5
v=20.
nx=30
nt=100
lenside=1000.
start1=2.*dx

def shape1(solution1,end1,x,start1=0):
    if method1==1:
        if start1 == 0.:
            start2=0.
        else:
            start2=np.mod(start1,end1) 
        
        solution1[:]=0.
        # top
        ind=np.where((x>=start2) & (x<(lenside/2.+start2))) 
        solution1[ind]=x[ind]-start2
        ind1=np.where((x>=(lenside/2.+start2)) & (x<(lenside+start2))) 
        solution1[ind1]=lenside-(x[ind1]-start2)
        
        # bottom
        start2=start2-end1
        ind=np.where((x>=start2) & (x<(lenside/2.+start2))) 
        if len(ind):
            solution1[ind]=x[ind]-start2
        ind1=np.where((x>=(lenside/2.+start2)) & (x<(lenside+start2))) 
        if len(ind1):
            solution1[ind1]=lenside-(x[ind1]-start2)
    if method1==2:
        if start1 == 0.:
            start2=0.
        else:
            start2=np.mod(start1,end1) 
        
        solution1[:]=0.
        # top
        ind=np.where((x>=start2) & (x<(lenside+start2))) 
        solution1[ind]=10.
        
        # bottom
        start2=start2-end1
        ind=np.where((x>=start2) & (x<(lenside+start2))) 
        if len(ind):
            solution1[ind]=10.
    return solution1


"""
    set up arrays
"""
x=np.mgrid[0.:dx*nx:dx]
solution=np.zeros(np.shape(x))
solution=shape1(solution,x[-1]+dx,x,start1)
    

solution1=np.zeros(np.shape(x))
solution1=shape1(solution1,x[-1]+dx,x,start1)

uxm = np.zeros(np.shape(solution))
uxp = np.zeros(np.shape(solution))

ap=np.max((v,0))
am=np.min((v,0))

username=getpass.getuser()
if not os.path.exists('/tmp/' + username):
         os.mkdir('/tmp/' + username)
os.system('rm /tmp/' + username + '/*')



"""
    solve using 1st order upwind over nt time-steps
"""
fig=plt.figure()
for j in range(nt):
    start1=start1+v*dt
    uxm[1:]=(solution[1:]-solution[:-1])/dx
    uxm[0]=(solution[0]-solution[-1])/dx
    
    uxp[:-1]=(solution[1:]-solution[:-1])/dx
    uxp[-1]=(solution[0]-solution[-1])/dx
    
    solution=solution-dt*(ap*uxm-am*uxp)        
    
    solution1=shape1(solution1,x[-1]+dx,x,start1)
    if j==0:
        line1,=plt.plot(x,solution)
        line2,=plt.plot(x,solution1,'--')
        plt.xlim((0,x[-1]))
        plt.xlabel('x (m)')
        plt.ylabel('transported variable (e.g. pollution level)')
        plt.legend(['upwind method','analytical method'])
    else:
        line1.set_ydata(solution)
        line2.set_ydata(solution1)
        fig.canvas.draw()
        fig.canvas.flush_events()
        
    plt.title('time: ' + str(dt*(j+1))+ 's')
    """
     print the plot to a directory
    """
    plt.savefig('/tmp/' +username + '/plot%03d.png' % j,format='png') 

plt.close()
    
os.system('convert -delay 20 /tmp/' +username + '/plot*.png /tmp/'\
     +username + '/animation.gif')    