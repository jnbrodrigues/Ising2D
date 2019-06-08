import numpy as np

def start_config(N,M):
    return np.random.randint(2,size=N*M).reshape((N,M))

print(start_config(3,3))

def grab_neighbors(i,j,config):
    return np.array([config[i-1,j],config[i+1,j],config[i,j+1],config[i,j-1])
    #return neighbors

    
def test_neighbors(config):
    i,j = 1,2
    assert grab_neighbors(i,j,config) == np.array([config[0,2],config[2,2],config[1,3],config[1,1]])
