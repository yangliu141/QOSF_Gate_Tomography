import numpy as np

def U3(theta, phi, lam):
    U11 = np.cos(theta/2)
    U12 = -np.exp(1j*lam) * np.sin(theta/2)
    U21 = np.exp(1j*phi) * np.sin(theta/2)
    U22 = np.exp(1j*(phi+lam)) * np.cos(theta/2)

    return np.array([[U11,U12],[U21,U22]])

def CNOT(control, target):
    cnot = np.eye(8)


    basis_states = [[0,0,0],
                    [0,0,1],
                    [0,1,0],
                    [0,1,1],
                    [1,0,0],
                    [1,0,1],
                    [1,1,0],
                    [1,1,1]]
    
    for i in range(8):
        control_bit = basis_states[i][control]

        if control_bit == 1:
            state_copy = basis_states[i].copy()
            state_copy[target] = 1 - state_copy[target] #Flip the qubit

            j = basis_states.index(state_copy)

            cnot[i,i] = 0
            cnot[j,i] = 1
    return cnot
 

def I():
    return np.eye(2)

def T():
    return np.array([[1,0],[0, np.exp(1j * np.pi / 4)]])

#Hadamard Gate
def H():
    return 1/np.sqrt(2)*np.array([[1,1],[1,-1]])

#Toffoli gate 
def Tof():

    tof = np.eye(8)

    #Flips target when both control are 1

    tof[6, 6] = 0
    tof[7, 6] = 1
    tof[7, 7] = 0  
    tof[6, 7] = 1
    
    return tof