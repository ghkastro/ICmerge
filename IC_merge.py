# IC_merge.py
# This code merges your GANDALF IC files and changes the x,y,z vectors if required, needed.
# It does not check physics, you have to check the physics yourself
# For any comments visit github.com/ghkastro


import numpy as np
import os
#from pathlib import Path


#-----------------------------------------------------
# Function for the number of objects you want to merge
#-----------------------------------------------------
def number_IC(n):
    print('Correct number?', n)
    cont = input('Yes = 1, No = 0\n')
    
    if cont == 1:
        print('OK')
    else:
        n = input('Last chance: ')

#----------------------------------------
# Function to add the path to your object
#----------------------------------------
def findPath(n):
    i = 0
    while i < n:
        totalpath = (input('Are your objects in one path?'))
        if totalpath == 1:
            path = os.path.abspath(raw_input('Path to your objects: '))
        #path = input('Path to your object: ')
        if i == 0:
             allobjs = (i)
             allpaths = (path)
        else:
            allobjs.append(i)
            allpaths.append(path)
        allobs = [allobjs, allpaths]
        print(allobs)
        f = open(path,'r+') #open file as read and write
        print('Do you want to change the position/location/distance of this object?')
        change_dist = input('Yes = 1, No = 0\n')
        if change_dist == 1:
            print('The distances has to be the same dimension as set in the generated IC!')
            x_dist = float(input("x distance:"))
            y_dist = float(input("y distance:"))
            z_dist = float(input("z distance:"))
            header_formatID = f.readline()
            header_pr = f.readline()
            header_ndim = f.readline()
            header_vdim = f.readline()
            header_mdim = f.readline()
            particle_n = f.readline()
            NHydro = "particle_n"
            c = StringIO("particle_n")
            np.loadtxt(c)
            #int("particle_n")
            NHydro = NHydro + 10000000
            #np.Nhydro(particle_n)
            print(NHydro)
            print(particle_n)
            for line in f:
                print(repr(line))
                line = line.strip()
                columns = line.split()
                #particle_n = f.line(5)
                line(219+particle_n)
                #line = [:+x_dist,:+y_dist,:+z_dist]
                # read in the file
                # check for the first line, the number of particles
                # particle_n = second line of the ascii file
                # go to file line number: xyz_vec = title(=1) + additional lines + particle_n
                # add numpy array changing the first set of x,y,z
                # for k < particle_n:
                #     if x_dist != 0:
                #         vector = (:'x_dist',:,:)
                #         if y_dist != 0:
                #         vector = (:,:'y_dist',:)
                #             if z_dist != 0:
                #             vector = (:,:,:'z_dist')
                #     elif y_dist != 0:
                #         vector = (:,:'y_dist',:)
                #         if z_dist != 0:
                #         vector = (:,:,:'z_dist')
                #     elif z_dist != 0:
                #         vector = (:,:,:'z_dist')
                #     else:
                #         print('No changes made!')
                #rename the filestring by adding x_dist, y_dist, z_dist
            print('File ', i, ' with path ', path,' was changed to: ', rename)
        f.close()
        i = i+1
        
# probably add function getting max of the vetor files and warn if overlap could happen
#
#
#
#
print('#==============================================================================================#')
print('#                                          IC_merge                                            #')
print('#                                                                                              #')
print('#   IC_merge merges your Initial Condition files produced by GANDALF written by Hubber et al.  #')
print('#       For more information on GANDALF please visit https://gandalfcode.github.com            #')
print('#  IC_merge does not check any physical terms or reasonable configuration of your merged files #')
print('#                  and does not guarantee proper physical initial condition.                   #')
print('#                               Written by G. Herbst-Kiss 2018                                 #')
print('#==============================================================================================#\n')
print('\n')
n = input('Number of objects you want to merge: ')
number_IC(n)
print('\n')
findPath(n)

