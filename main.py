import numpy as np
import matrixFunctions as mF

# Add origin unit vectors
origin = np.array([ [0,1],   # x
                    [0,1],   # y
                    [0,1] ]) # z

# Create rotaton matrix around z axis
Rmz = mF.rotateMatrix(np.deg2rad(90), 'z')

# Rotate origin with rotation matrix
Rorigin = np.dot(Rmz, origin)

# Plot rotated origin
mF.plotVectors(Rorigin)