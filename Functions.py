import numpy as np
from Gates import U3, CNOT, T, H, I

#Tensor product of a list of 3 single-qubit gates
def tensor(gate_list):
    A = gate_list[0]
    B = gate_list[1]
    C = gate_list[2] 
    return np.kron(np.kron(A,B),C)



#Function for applying a single qubit gate on qubit q to a 8x8 Unitary U
def apply_sqg(U,gate,qubit):
    matrix = [I(), I(), I()]
    matrix[qubit] = gate

    return tensor(matrix)@U



#Function for applying CNOT with control = c and target = t to a Unitary U
def apply_cnot(U, c, t):
    cnot = CNOT(c, t)
    return cnot @ U



def create_circuit_Unitary(p):

    #Gates 
    T_gate = T()
    T_ad = T_gate.conj().T
    H_gate = H()

    #Unitary for the circuit
    U = np.eye(8)

    #The two U3 gates
    U3_1 = U3(p[0], p[1], p[2])
    U3_2 = U3(p[3], p[4], p[5])


    #Constructing the Unitary for the circuit
    U = apply_sqg(U,T_gate,0)
    U = apply_sqg(U,U3_1,2)

    U = apply_cnot(U,0,1)
    U = apply_sqg(U, T_ad,1)
    U = apply_cnot(U,0,1)
    U = apply_sqg(U, T_gate,1)

    U = apply_cnot(U,1,2)
    U = apply_sqg(U, T_ad,2)
    U = apply_cnot(U,0,2)
    U = apply_sqg(U, T_gate, 2)
    U = apply_cnot(U,1,2)

    U = apply_sqg(U,U3_2,2)
    U = apply_cnot(U,0,2)
    U = apply_sqg(U, T_gate, 2)
    U = apply_sqg(U, H_gate, 2)

    return U
    

