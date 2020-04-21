import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

cos = np.cos
sin = np.sin
pi = np.pi

def rotateMatrix(th, axis):
    # th: angle in radians to rotate
    # axis: in which axis is going to be rotated, must be 'x', 'y' or 'z'
    if axis=='x':
        M = np.array([ [1,        0,         0], 
                     [   0, cos(th),  -sin(th)], 
                     [   0, sin(th),   cos(th)] ])
    elif axis=='y':
        M = np.array([ [cos(th),   0, sin(th)], 
                     [        0,   1,       0], 
                     [ -sin(th),   0, cos(th)] ])
    elif axis=='z':
        M = np.array([ [cos(th), -sin(th),   0], 
                     [  sin(th),  cos(th),   0], 
                     [       0,        0,    1] ])
    return M

def plotVectors(vectorMatrix):
    # input "vectorMatrix" must be a 3x2 matrix where each row 
    # has the first and second coordinate of a vector on x, y and z
    fig = plt.figure()
    fig.suptitle('Origin Plot', fontsize=16)
    ax = plt.axes(projection='3d')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.plot(vectorMatrix[0,:],[0, 0],[0, 0], 'r') # [x1 x2], [y1 y2], [z1 z2]
    ax.plot([0, 0],vectorMatrix[1,:],[0, 0], 'g')
    ax.plot([0, 0],[0, 0],vectorMatrix[2,:], 'b')
    plt.show()
