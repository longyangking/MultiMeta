import numpy as np
import numpy.linalg as linalg

class Bandstructure:
    def __init__(self,materials,ds,frequencys):
        self.materials = materials
        self.ds = ds
        self.frequencys = frequencys
        
    def bulkbands(self,kstart,kend):
        
    def eigenvalues(self,k):
        
    def eigenstates(self,k):

    def eigensystem(self,k):
        hamiltonian = self.__hamiltonianbulk(k)
        eigenValues,eigenVectors = linalg.eigs(hamiltonian)
        eigenValues = np.sqrt(eigenValues)/2/np.pi
        return eigenValues,eigenVectors

    def edgebands(self,kstart,kend,axis=0,background=None):
        
    def eigenvaluesedge(self,k,axis,background=None):
        
    def eigenstatesedge(self,k,axis,background=None):

    def eigensystemedge(self,k,axis,background=None): 

    def __hamiltonianbulk(self,k):
        
        
    def __hamiltonianedge(self,k,axis,background):