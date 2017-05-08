import numpy as np
import numpy.linalg as linalg

class Bandstructure:
    def __init__(self,materials,ds,frequencys):
        self.materials = materials
        self.ds = np.array(ds)
        self.frequencys = frequencys

        self.a = np.sum(self.ds)
        self.layersnum = len(materials)
        
    def bulkbands(self):
        M = np.size(self.frequencys)
        bands = list()
        for i in range(M):
            frequency = self.frequencys[i]
            Ka,eigenvectors,code = self.eigensystem(i)
            if code:
                bands.append([Ka/self.a,frequency])
                bands.append([-Ka/self.a,frequency])
        return np.array(bands)

    def eigensystem(self,frequencypoint):
        hamiltonian = self.__hamiltonianbulk(frequencypoint)
        eigenValues,eigenVectors = linalg.eig((hamiltonian + linalg.inv(hamiltonian))/2)
        #eigenValue = np.mean(np.abs(eigenValues))
        eigenValue = np.max(eigenValues)
        if np.abs(eigenValue) > 1:
            return None,None,False
        return np.arccos(eigenValue),eigenVectors,True

    def edgebands(self,kstart,kend,axis=0,background=None):
        pass
        
    def eigenvaluesedge(self,k,axis,background=None):
        pass

    def eigenstatesedge(self,k,axis,background=None):
        pass

    def eigensystemedge(self,k,axis,background=None): 
        pass

    def __hamiltonianbulk(self,frequencypoint):
        frequency = self.frequencys[frequencypoint]
        c = 3.0*10**8

        epsilon = np.zeros(self.layersnum,dtype=complex)
        mur = np.zeros(self.layersnum,dtype=complex)
        Z = np.zeros(self.layersnum,dtype=complex)
        n = np.zeros(self.layersnum,dtype=complex)
        for i in range(self.layersnum):
            epsilon[i] =  self.materials[i].epsilon[frequencypoint]
            mur[i] = self.materials[i].mur[frequencypoint]
            Z[i] = np.sqrt(mur[i]/epsilon[i])
            n[i] = np.sqrt(epsilon[i]*mur[i])

        Q = np.eye(2,dtype=complex)
        for i in range(self.layersnum):
            j = (i+1)%self.layersnum
            P = np.array([[1+Z[j]/Z[i], 1-Z[j]/Z[i]], \
                        [1-Z[j]/Z[i], 1+Z[j]/Z[i]]],dtype=complex)/2

            phase = n[i]*2.0*np.pi*frequency/c*self.ds[i]
            M = np.array([[np.exp(1j*phase), 0], \
                        [0, np.exp(-1j*phase)]],dtype=complex)

            Q = P.dot(M.dot(Q))
        
        return Q
                    
    def __hamiltonianedge(self,k,axis,background):
        pass