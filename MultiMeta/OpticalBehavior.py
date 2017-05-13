import numpy as np 
from Material import Material

class OpticalBehavior:
    def __init__(self,materials,ds,frequencys,background=None):
        self.materials = materials
        self.ds = ds

        self.layersnum = len(ds)
        self.frequencys = frequencys

        M = np.size(frequencys)
        if background is None:
            self.background = Material(frequencys,np.ones(M),np.ones(M))
        else:
            self.background = background

    def TR(self,angle=0):
        c = 3.0*10**8
        M = np.size(self.frequencys)
        t = np.zeros(M,dtype=complex)
        r = np.zeros(M,dtype=complex)

        Z = np.zeros(self.layersnum + 2,dtype=complex)
        n = np.zeros(self.layersnum + 2,dtype=complex)

        for frequencypoint in range(M):
            frequency = self.frequencys[frequencypoint]

            # Background Material
            epsilon =  self.background.epsilon[frequencypoint]
            mur = self.background.mur[frequencypoint]
            Z[0] = np.sqrt(mur/epsilon)
            n[0] = np.sqrt(epsilon*mur)
            Z[self.layersnum+1] = np.sqrt(mur/epsilon)
            n[self.layersnum+1] = np.sqrt(epsilon*mur)

            # Material Layers
            for i in range(1,self.layersnum + 1):
                epsilon =  self.materials[i - 1].epsilon[frequencypoint]
                mur = self.materials[i - 1].mur[frequencypoint]
                Z[i] = np.sqrt(mur/epsilon)
                n[i] = np.sqrt(epsilon*mur)

            # Calculate TR
            Q = np.eye(2,dtype=complex)
            for i in range(1,self.layersnum + 2):
                P = np.array([[1+Z[i]/Z[i-1], 1-Z[i]/Z[i-1]], \
                              [1-Z[i]/Z[i-1], 1+Z[i]/Z[i-1]]],dtype=complex)/2

                if i == self.layersnum + 1:
                    phase = 0
                else:
                    phase = n[i]*2.0*np.pi*frequency/c*self.ds[i-1]
                M = np.array([[np.exp(1j*phase), 0], \
                            [0, np.exp(-1j*phase)]],dtype=complex)

                Q = M.dot(P.dot(Q))
            
            t[frequencypoint] = -(Q[0,1]*Q[1,0]-Q[0,0]*Q[1,1])/Q[1,1]
            r[frequencypoint] = -Q[1,0]/Q[1,1]
            
        return t,r