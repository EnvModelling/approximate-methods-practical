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
    a simple python script to plot the analytical solution to d2y/dt2=-omega^2 y
"""

"""
    parameters for the simulation - these are the lines you should change+++++++++++++++++
"""
method1=1
omega1=0.1
y0=5
dy0=0.
dt=1.
tend=100.
tinit=0.
dtsolve=0.5
"""
------------------------------------------------------------------------------------------
"""


"""
 create arrays
"""
ts=np.mgrid[tinit:tend+dt:dt] 
tsolve=np.mgrid[tinit:tend+dtsolve:dtsolve] 
solution1=np.zeros(np.shape(tsolve)) # y
solution2=np.zeros(np.shape(tsolve)) # dy
"""
---------------
"""


"""
 create handle for plot and plot
"""
fig=plt.figure()
plt.plot(ts,y0*np.cos(omega1*ts))
plt.xlabel('time (s)')
plt.ylabel('displacement')
"""
---------------
"""


if method1==1:
    """
     SOLVE USING THE FORWARD EULER METHOD
    """
    solution1[0]=y0
    solution2[0]=dy0
    for i in range(len(solution1)-1):
        solution2[i+1]=solution2[i]+dtsolve*-omega1**2*solution1[i]
        solution1[i+1]=solution1[i]+dtsolve*solution2[i]
    text1='Forward Euler solution with $\Delta t=' + str(dtsolve) +'$'
# elif method1==2:
#     """
#      SOLVE USING THE FORWARD EULER METHOD FOR FIRST STEP AND THEN CENTRED
#     """
#     solution[0]=N0
#     for i in range(len(solution)-1):
#         if i==0:
#             solution[i+1]=solution[i]+dtsolve*-lambda1*solution[i]
#         else:
#             solution[i+1]=solution[i-1]+2*dtsolve*-lambda1*solution[i]
#     text1='Centred Difference solution with $\Delta t=' + str(dtsolve) +'$'
    
    

"""
plot solution
"""
plt.plot(tsolve,solution1,'--')


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