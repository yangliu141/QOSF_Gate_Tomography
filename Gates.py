import numpy as np


#General single-qubit gate
def U3(theta, phi, lam):
    U11 = np.cos(theta/2)
    U12 = -np.exp(1j*lam) * np.sin(theta/2)
    U21 = np.exp(1j*phi) * np.sin(theta/2)
    U22 = np.exp(1j*(phi+lam)) * np.cos(theta/2)

    return np.array([[U11,U12],[U21,U22]])

#CNOT-gate acting on a 3-qubit system
#Input: index of control qubit, index of target qubit
def CNOT(control, target):

    #8x8-matrix
    cnot = np.eye(8)

    #All computational basis states
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

        #Only flip target qubit when control is 1
        if control_bit == 1:

            #Flip target qubit
            state_copy = basis_states[i].copy()
            state_copy[target] = 1 - state_copy[target]  


            #Index of the new basis state 
            j = basis_states.index(state_copy)

            #Update CNOT matrix
            cnot[i,i] = 0
            cnot[j,i] = 1
    return cnot
 
#Identity gate
def I():
    return np.eye(2)

#T-gate
def T():
    return np.array([[1,0],[0, np.exp(1j * np.pi / 4)]])

#Hadamard Gate
def H():
    return 1/np.sqrt(2)*np.array([[1,1],[1,-1]])

#Toffoli gate (Control: 0, 1. Target: 2)
def Tof():

    #8x8-matrix
    tof = np.eye(8)

    #Flips target when both control qubits are 1

    tof[6, 6] = 0
    tof[7, 6] = 1
    tof[7, 7] = 0  
    tof[6, 7] = 1
    
    return tof