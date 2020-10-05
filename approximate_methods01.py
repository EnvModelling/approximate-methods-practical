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
    a simple python script to plot the analytical solution to dy/dt=-lambda y
"""

"""
    parameters for the simulation
"""
method1=1
lambda1=1./2e3
N0=1e20
dt=1.
tend=1e4
tinit=0.
dtsolve=10.


"""
 create arrays
"""
ts=np.mgrid[tinit:tend+dt:dt] 
tsolve=np.mgrid[tinit:tend+dtsolve:dtsolve] 
solution=np.zeros(np.shape(tsolve))


"""
 create handle for plot and plot
"""
fig=plt.figure()
plt.plot(ts,N0*np.exp(-lambda1*ts))
plt.xlabel('time (s)')
plt.ylabel('number of atoms')


if method1==1:
    """
     SOLVE USING THE FORWARD EULER METHOD
    """
    solution[0]=N0
    for i in range(len(solution)-1):
        solution[i+1]=solution[i]+dtsolve*-lambda1*solution[i]
    text1='Forward Euler solution with $\Delta t=' + str(dtsolve) +'$'
elif method1==2:
    """
     SOLVE USING THE FORWARD EULER METHOD FOR FIRST STEP AND THEN CENTRED
    """
    solution[0]=N0
    for i in range(len(solution)-1):
        if i==0:
            solution[i+1]=solution[i]+dtsolve*-lambda1*solution[i]
        else:
            solution[i+1]=solution[i-1]+2*dtsolve*-lambda1*solution[i]
    text1='Centred Difference solution with $\Delta t=' + str(dtsolve) +'$'
    
    

"""
plot solution
"""
plt.plot(tsolve,solution,'--')


plt.legend(['Analytical solution',text1])
"""
 print the plot to a directory
"""
username=getpass.getuser()
if not os.path.exists('/tmp/' + username):
         os.mkdir('/tmp/' + username)
os.system('rm /tmp/' + username + '/*')
plt.savefig('/tmp/' +username + '/plot%03d.png' % method1,format='png') 
plt.close()