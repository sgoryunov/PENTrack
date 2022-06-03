#!/usr/bin/env python3
from distutils.log import debug
from functools import partial
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt


def main():
   
    

    # m_partial = 
    t = []
    x = []
    y = []
    z = []
    vx = []
    vy = []
    vz = []
    x0 = []
    y0 = []
    z0 = []
    bx0 = []
    by0 = []
    bz0 = []
    
    try:

        with open ('comsolField.txt',"r") as f1:
            lines = f1.readlines()[8:]
            for num, line in enumerate(lines):
                text = line.split()
                x0.append(float( text[0]) )
                y0.append(float( text[1]) )
                z0.append(float( text[2]) )
                bx0.append(float( text[3]) )
                by0.append(float( text[4]) )
                bz0.append(float( text[5]) )
        # fig3 = plt.figure(3)
        ax = plt.figure(1).add_subplot(projection='3d')
        ax.quiver(x0, y0, z0, bx0, by0, bz0, length=0.3, normalize=True)
        plt.title('Vector Field zy plane (Original COMSOL)')
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        # plt.show()
    except IOError:
        print("Can't find comsolField.txt... skipping plot")

    try:
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        neutr_num = 1
        with open ('000000000000neutrontrack.out',"r") as f1:
            lines = f1.readlines()[1:]
            for num, line in enumerate(lines):
                text = line.split(" ")
                if int(text[1]) != neutr_num:
                    ax.plot3D(x, y, z, 'green')
                    x = []
                    y = []
                    z = []
                    neutr_num = int(text[1])
                t.append(float( text[3]) )
                x.append(float( text[4]) )
                y.append(float( text[5]) )
                z.append(float( text[6]) )
                vx.append(float( text[7]) )
                vy.append(float( text[8]) )
                vz.append(float( text[9]) )
        
        ax.plot3D(x, y, z, 'green')
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        print(f'Neutron number is {neutr_num}')
        # plt.show()
    except IOError:
        print("Can't find BFCut.out... skipping plot")
    
    plt.show()  
    return

if ( __name__ == '__main__' ):
    main()
