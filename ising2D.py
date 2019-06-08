import numpy as np

def start_config(N,M):
    '''Start config.'''
    return np.random.randint(2,size=N*M).reshape((N,M))


def grab_neighbors(i,j,config):
    '''Grab neighbors with PBCs'''
    
    confsh=config.shape
    N,M=confsh[0],confsh[1]

    top = [i-1 if i-1>=0 else N-1, j ]
    bottom = [(i+1)%N,j]
    left = [i,j-1 if j-1>=0 else M-1]
    right = [i,(j+1)%M]

    return np.array([config[top[0],top[1]],config[bottom[0],bottom[1]],config[right[0],right[1]],config[left[0],left[1]]])


    
