import numpy as np

class Material:
    def __init__(self,frequencys,epsilon=None,mur=None):
        self.frequencys = frequencys
        
        if epsilon is None:
            self.epsilon = 1.0*np.ones(len(self.frequencys))
        else:
            self.epsilon = epsilon

        if mur is None:
            self.mur = 1.0*np.ones(len(self.frequencys))
        else:
            self.mur = mur

    def set_epsilon_drude(self, fw, ftau):
        self.epsilon = 1 - np.square(fw)/(np.square(frequencys) + 1j*ftau*frequencys)
    
    def set_mur_drude(self, fw, ftau):
        self.mur = 1 - np.square(fw)/(np.square(frequencys) + 1j*ftau*frequencys)

    def set_epsilon_lorentz(self, fw, f0, ftau):
        self.epsilon = 1 - np.square(fw)/(-np.square(f0) + np.square(frequencys) + 1j*ftau*frequencys)
    
    def set_mur_lorentz(self, fw, f0, ftau):
        self.mur = 1 - np.square(fw)/(-np.square(f0) + np.square(frequencys) + 1j*ftau*frequencys)
