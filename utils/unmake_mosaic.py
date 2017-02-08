import numpy as np

def unmake_mosaic(mosaic, side=None):
    images = []
    h = mosaic.shape[0]
    w = mosaic.shape[1]
    nx = w / side
    ny = h / side
    w = side
    h = side
    for i in range(ny):
        ia = (i)*h
        ib = (i+1)*h
        for j in range(nx):
            ja = j*w
            jb = (j+1)*w
            images.append(mosaic[ia:ib, ja:jb])
    return np.array(images)