import numpy as np
import ising2D

def test_neighbors():
    i,j = 1,2
    config = ising2D.start_config(3,4)                
    assert (ising2D.grab_neighbors(i,j,config) == np.array([config[0,2],config[2,2],config[1,3],config[1,1]])).all()

def test_neighbours_pbc():
    N,M=3,4
    config = ising2D.start_config(N,M)                
    assert (ising2D.grab_neighbors(N-1,M-1,config) == np.array([config[N-2,M-1],config[0,M-1],config[N-1,0],config[N-1,M-2]])).all() 
