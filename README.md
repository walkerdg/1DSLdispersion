# 1DSLdispersion
Calculate the one-dimensional phonon dispersion of a superlattice

The input gives the relative size of the masses in a one-dimensional chain arranged in a superlattice.  The lattice can have mulitple types of layers each delineated with square brackets.  The unit is quare brackets is multiplies the specified number of time to create a single layer.  All layers are grouped in round brackets and multiplied by any number of times.  

m = 10*(3*[1] + 4*[2, 3])

This means that the superlattice has two layer.  One layer has one mass per unit cell and the unit cell is repeated three time.  The other layer has two masses.  One is twice as big as the mass in layer one; the other is 3 times as big as the one in layer one.  The sum of these two layers is the unit cell of the superlattice, which is repeated 10 times.  Theoretically, the solution does not require that the superlattice be repeated.  However, the number of wavevectors will be smaller and so the dispresion will not be a continuous.  
