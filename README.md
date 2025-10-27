# QOSF - Screening task Cohort 11

## Description 

This repository contains my solution to the Screening Task 1 - Gate Tomography for the QOSF Mentorship program Cohort 11.

The objective of the task is to determine the hidden parameters of two unknow U3 gates in a quantum circuit such that the circuit becomes equivalent to a Toffoli gate. 
My results show that the hidden parameters are: 
- U3($\frac{\pi}{2}, 0, \pi$) for the first gate 
- U3($0, 0, -\frac{\pi}{4}$) for the second gate

This is equivalent to a $H$-gate and a $T^\dagger$-gate.

Here you will find instructions on how to clone, install and run the necessary files. In addition to a structured overview of the folders and files.

## Project Prerequisites
Before installation, make sure you have:
- Python 3.10 or higher
- pip 22+
- Git
- Jupyter Notebook or Jupyterlab (for `.ipynb` notebooks)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yangliu141/QOSF_Gate_Tomography.git
   cd QOSF_Gate_Tomography
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the project:
   ```bash
   jupyter notebook Results.ipynb
   ```

## Description and Structure of `Code/`

### `Gates.py`
- Implements quantum gates using NumPy arrays
### `Functions.py`
- Contains functions for building the unitary for the custom circuit
### `Results.ipynb`
- Parameter search for the hidden U3 gates
- Visualization and comparison to Qiskit´s Toffoli gate decomposition
