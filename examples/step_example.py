from pylab import *
from scipy import *

import controls
reload(controls)


##############################
#
#  Plotting a step response
#
##############################

# define parameters
wn = 3.0
z = 0.2

#create a TransferFunction instance
tf = controls.TransferFunction(wn**2,[1,2*z*wn,wn**2])

#calculate the step response and plot it
y, t, u = tf.step_response(fignum=1)



######################################
#
#  Laplace analysis of step response
#
######################################
U = controls.Input(1,[1,0])
Y = tf*U
r,p,k = Y.residue()
tflist = Y.PartFrac()
print('r='+str(r))
print('p='+str(p))
print('k='+str(k))
print('partial fraction expansion = \n'+str(tflist))

show()
