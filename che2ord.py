#che2ord.py
#Andrew R Garcia, Dec. 2014
import numpy as np
import matplotlib.pylab as plt
import scipy.linalg as lin
'''The Chemical Engineering Eigenvalue problem: Transdermal Drug Diffusion with Python
Andrew Garcia, 2015
https://www.youtube.com/watch?v=ZQMt8kuVvIM
'''

def eig(phi):
    'Return eigenvalues and corresp. eigenvectors'
 
    A = [[0,1],
         [phi**2,0]]

     
    lmda,E = lin.eig(A)
    
    return lmda,E
    

def build(phi):
    '''Build solution to differential
    e.g. "x(t)=C1*exp(lambda1*t)+C2*exp(lambda2*t)'''
    
    [lmda,E]=eig(phi)
    
    G0=[1,0]
    #E c = G0
    c=lin.solve(E,G0)
    
    xi=np.arange(0,1,0.01)
    Theta=E[0,0]*c[0]*np.exp(lmda[0]*xi)+E[0,1]*c[1]*np.exp(lmda[1]*xi)
    
    
    plt.plot(xi,Theta)
    plt.xlabel('$\\xi$=x/L',size=15)
    plt.ylabel('$\Theta=C_D/C_f$',size=15)

build(1)
    