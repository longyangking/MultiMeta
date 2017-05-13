import sys
sys.path.append('..')

import numpy as np 
import MultiMeta
import matplotlib.pyplot as plt 

if __name__ == '__main__':
    num = 500
    f0 = 10.0*10**9
    lambda0 = 3.0*10**8/f0
    frequencys = f0*np.linspace(0.01,2,num)
    material1 = MultiMeta.Material(frequencys,4.0*np.ones(num),1.0*np.ones(num))
    material2 = MultiMeta.Material(frequencys,1.0*np.ones(num),1.0*np.ones(num))

    periods = 10
    materials = [material1,material2]*periods
    ds = [lambda0/4/np.sqrt(4.0),lambda0/4]*periods
    a = np.sum(ds)
    multilayer = MultiMeta.OpticalBehavior(materials,ds,frequencys)

    t,r = multilayer.TR()

    fig = plt.figure()
    T = plt.plot(frequencys/f0,np.square(np.abs(t)),label="T")
    R = plt.plot(frequencys/f0,np.square(np.abs(r)),label="R")
    plt.legend(["Transmission", "Reflection"], loc=1)
    plt.title('Optical behavior of 1D photonics crystal')
    plt.xlabel('Frequency/$f_0$')
    plt.ylim(0,1)
    plt.show()