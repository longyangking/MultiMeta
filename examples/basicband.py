import sys
sys.path.append('..')

import numpy as np 
import MultiMeta
import matplotlib.pyplot as plt 

if __name__ == '__main__':
    num = 200
    f0 = 10.0*10**9
    lambda0 = 3.0*10**8/f0
    frequencys = f0*np.linspace(0.01,3,num)
    material1 = MultiMeta.Material(frequencys,4.0*np.ones(num),1.0*np.ones(num))
    material2 = MultiMeta.Material(frequencys,1.0*np.ones(num),1.0*np.ones(num))

    materials = [material1,material2]
    ds = [lambda0/4/np.sqrt(4.0),lambda0/4]
    a = np.sum(ds)
    bandstructure = MultiMeta.Bandstructure(materials,ds,frequencys)

    bulkbands = bandstructure.bulkbands()

    fig2 = plt.figure()
    plt.scatter(a*bulkbands[:,0],bulkbands[:,1]/f0)
    plt.title('1D photonics crystal bulk-band structure')
    plt.xlabel('$Ka$')
    plt.ylabel('Frequency/$f_0$')
    plt.xlim(-3.14,3.14)
    plt.ylim(0,3)
    plt.show()