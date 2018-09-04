# Using lattice dynamics (eigenvalues of the dynamical matrix),
# calculate the phonon dispersion in a one-dimensional chain.
# Everything is implicitly normalized.  

# Greg Walker (adapted from Casey Brock)

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal


############
# Inputs ...

# Build the dynamical matrix.  This is where the magic happens.  
m = 2*(100*[1.0, 1.0] + 100*[1.3, 0.5])
# number of nearest neighbors (normally keep this at 1)
Nn = 1

#####################
# Computed parameters

N = len( m )
print( N )

A = np.zeros((N,N))
# the loop is for the number of nearest neighbors using an exponential decay to
# attenuate the effect of far away atoms, For Nn = 1, the exponential is unity.
for i in range( 1, Nn+1 ):
    Ai = 2*np.diagflat( m )
    Ai -= np.diagflat( m[:-i], i )
    Ai -= np.diagflat( m[i:], -i )
    Ai -= np.diagflat( m[:i], N-i )
    Ai -= np.diagflat( m[-i:], -(N-i) )
    A += np.exp(-(i-1)) * Ai
    
# sanity checks ...
#print(A)
#print( np.sum(np.sum( A )) )

###############
# Calculate ...
 
# Solve the eigenvalue problem
lam,v = np.linalg.eig( A )

# Convert to w vs. k for plotting
omega = np.zeros( N )
k = np.zeros( N )

# How to order the eigenvalues based on the eigenvectors (select your favorite
# window filter

#window = scipy.signal.kaiser(N, 2, sym=True)
window = scipy.signal.cosine(N, sym=True)
#window = scipy.signal.flattop(N, sym=True)

for i in range( N ):

    windowed = np.real( v[:,i] * window )
    k[i] = (2/N) * np.argmax( np.abs(np.fft.rfft( windowed )) )
    omega[i] = np.sqrt( np.abs( np.real(lam[i]) ) ) / 2

############
# Output ...

plt.plot( k, omega, '.' )
plt.grid()
plt.xlabel( 'wavevector' )
plt.ylabel( 'frequency' )
plt.show()

f = open( "dispersion.dat", "w" )
for i in range( N ):
    f.write( str(k[i]) + " " + str(omega[i]) + "\n" )
f.close()


