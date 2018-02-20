# IC_merge.py
# This code merges your GANDALF IC files and changes the x,y,z vectors if required, needed.
# It does not check physics, you have to check the physics yourself
# For any comments visit github.com/ghkastro
# -*- coding: utf-8 -*-

import csv
import numpy as np
import os
from astropy.extern.six.moves import cStringIO as StringIO
# -*- coding: utf-8 -*-
#from pathlib import Path


#-----------------------------------------------------
# Function for the number of objects you want to merge
#-----------------------------------------------------
def number_IC():
    total_n = input('Number of objects you want to merge: ')

#----------------------------------------------
# Changing the distances of your chosen objects
#----------------------------------------------
def change_distance(fullpath):
    print(fullpath)
    print('----------------------------------------------------------------------')
    print('The distances has to be the same dimension as set in the generated IC!')
    print('----------------------------------------------------------------------')
    x_dist = float(input("x distance: "))
    y_dist = float(input("y distance: "))
    z_dist = float(input("z distance: "))
    f = open(fullpath,'r+')
    newfullpath = fullpath + 'x' + str(x_dist) + 'y' +str(y_dist) + 'z' + str(z_dist)
    print(newfullpath)
    nf = open(newfullpath,'w')
    #nf = newfile with new name
    # nf.write the header and alle the other data, will need a loop for that and than the new vectors
    #
    #
    header_formatID = f.readline()
    header_pr = f.readline()
    header_ndim = f.readline()
    header_vdim = f.readline()
    header_bdim = f.readline()
    Nhydro = f.readline()
    nf.write(header_formatID)
    nf.write(header_pr)
    nf.write(header_ndim)
    nf.write(header_vdim)
    nf.write(header_bdim)
    nf.write(Nhydro)
    data = []
    NHydro = Nhydro
    print(NHydro)
    print(Nhydro)
    int(Nhydro)
    i = int(Nhydro) + 213 #where the position vector starts
    int(i)
    print(i)
    end_vec = int(i) + int(Nhydro) # 6 lines more than needed
    print(end_vec)
    for m,line in enumerate(f):
        if m < i:
            line = line.strip()
            line
            columns = line.split()
            columns
            nf.write(line)
            nf.write('\n')
 #   for k,line in enumerate(f):
        if m >= i and m < end_vec:# and k < end_vec:
            line = line.strip()
            line
            columns = line.split()
            columns
            if x_dist != 0 and y_dist != 0 and z_dist != 0:
                columns[0] = float(columns[0]) + x_dist
                columns[1] = float(columns[1]) + y_dist
                columns[2] = float(columns[2]) + z_dist
                columns[0] = str(columns[0])
                columns[1] = str(columns[1])
                columns[2] = str(columns[2])
                new_line = columns[0] + '   ' + columns[1] + '   ' + columns[2]
                nf.write(str(new_line))
                nf.write('\n')
                #print(columns[1])
                #print(columns[2])
            elif x_dist != 0 and y_dist != 0:
                columns[0] = float(columns[0]) + x_dist
                columns[1] = float(columns[1]) + y_dist
                columns[0] = str(columns[0])
                columns[1] = str(columns[1])
                columns[2] = str(columns[2])
                new_line = columns[0] + '   ' + columns[1] + '   ' + columns[2]
                nf.write(str(new_line))
                nf.write('\n')
                #print(columns)
            elif x_dist != 0 and z_dist != 0:
                columns[0] = float(columns[0]) + x_dist
                columns[2] = float(columns[2]) + z_dist
                columns[0] = str(columns[0])
                columns[1] = str(columns[1])
                columns[2] = str(columns[2])
                new_line = columns[0] + '   ' + columns[1] + '   ' + columns[2]
                nf.write(str(new_line))
                nf.write('\n')
                #print(columns)
            elif y_dist != 0 and z_dist != 0:
                columns[1] = float(columns[1]) + y_dist
                columns[2] = float(columns[2]) + z_dist
                new_line = columns[0] + '   ' + columns[1] + '   ' + columns[2]
                nf.write(str(new_line))
                nf.write('\n')
                #print(columns)
            elif z_dist != 0:
                columns[2] = float(columns[2]) + z_dist
                columns[0] = str(columns[0])
                columns[1] = str(columns[1])
                columns[2] = str(columns[2])
                new_line = columns[0] + '   ' + columns[1] + '   ' + columns[2]
                nf.write(str(new_line))
                nf.write('\n')
   # for o,line in enumerate(f):
        if m >= end_vec:
            line = line.strip()
            line
            columns = line.split()
            columns
            nf.write(line)
            nf.write('\n')
    nf.close()
    f.close()
    print'New Filename with distances: x = ', x_dist, ' y = ', y_dist, ' z = ', z_dist, '\n', newfullpath,'\n' 
    fullpath = newfullpath
    print('Newfullpath: ')
    print(newfullpath)
    print('+++++++++++++')
    print('Fullpath (should be same as newfullpath: ')
    print(fullpath)
    return newfullpath#, Nhydro


#-------------------------------------
# Get all object names and put in list
#-------------------------------------
def get_objects(path):
    n_objects = input('How many objects from this path? ')
    j=1
    j_list = []
    filenames = []
    #files = [j]
    print(path)
    while j <= n_objects:
        fileadd = raw_input('Filename: ')
        #filename.append(fileadd)
        j_list.append(j)
        fullpath = str(path) + '/' + str(fileadd)
        print(fullpath)
        
        #print(path, filename)
        changedist = input('Do you want to change the distance? Yes = 1, No = 0\n')
        if changedist == 1:
            fullpath = change_distance(fullpath)#,Nhydro)
            print('Passing the fullpath to get_objects: ')
            print(fullpath)
        filenames.append(fullpath)
        j = j+1
    merge_list = [j_list, filenames]
    print(merge_list[:])
    return fullpath#, Nhydro



#----------------------------------------
# Function to add the path to your object
#----------------------------------------
def findPath():
    totalpath = (input('In how many paths are your objects? '))
    k=0
    numberpaths=[]
    numberfullpath=[]
    #numberNhydro=[]
    merge_list = []

    if totalpath == 1:
        path = os.path.abspath(raw_input('Path to your objects: '))
        print(path)
        fullpath = get_objects(path)
        #Nhydro = get_objects(Nhydro)
        print('!!!!!!!!!!')
        print(fullpath)
            #1print(path, filename)
        #path = input('Path to your object: ')
        numberpaths.append(k)
        numberfullpath.append(fullpath)
        #numberNhydro.append(Nhydro)
        allpaths=[numberpaths,numberfullpath]#,numberNhydro]
    else:
        while (k <= totalpath-1):
            path = os.path.abspath(raw_input('Path to your objects: '))
            #if k > 0:
            fullpath = get_objects(path)
            #Nhydro = get_objects(Nhydro)
            print('###########')
            #print(merge_list[:])
            
            print(fullpath)
            var_paths = [k, fullpath]
            print(var_paths)
            print('*********')
            numberpaths.append(k)
            numberfullpath.append(fullpath)
            #numberNhydro.append(Nhydro)
            k = k+1
        allpaths=[numberpaths,numberfullpath]#,numberNhydro]
        print(allpaths)
    return allpaths
    #if totalpath == 1:
    #    allobjs = totalpath
    #    allpaths = fullpath
    #else:
    #    allobjs = totalpath
    #    allpaths.append(fullpath)
    #allobs = [allobjs, allpaths]   
    #print(allobs)

#-----------------------------------------------------
# Function to get max. NHydro file and merge all files
#-----------------------------------------------------

def merge():
    print'Merging all files'
    allpaths[:]
    numberNhydro=[]
    numberNstar=[]
    numberNgas=[]
    numberNcdm=[]
    numberNdust=[]
    numbermmean=[]
    typedata=[]
    numbertypedata=[]
    zero=0
    mmean=0
    sum_Nhydro = 0
    sum_Ngas = 0
    sum_Ndust = 0
    print(allpaths)
    me_fullpath = raw_input('Path to put the merged file: ')
    me_name = raw_input('Filename for the merged file: ')
    me_fullpath = me_fullpath + '/' + me_name
    #get all file paths and number of all NHydros
    i=0
    j=0
    q=np.amax(allpaths[0][:])
    print('q = ',q)
    while j <= q:
        print(allpaths[1][j])
        filename = str(allpaths[1][j])
        f = open(filename, 'r+')
        header_formatID = f.readline()
        header_pr = f.readline()
        header_ndim = f.readline()
        header_vdim = f.readline()
        header_bdim = f.readline()
        Nhydro = f.readline()
        Nstar = f.readline()
        NA = f.readline()
        NA = f.readline()
        Ngas = f.readline()
        Ncdm = f.readline()
        Ndust = f.readline()
        numberNhydro.append(Nhydro)
        numberNstar.append(Nstar)
        numberNgas.append(Ngas)
        numberNcdm.append(Ncdm)
        numberNdust.append(Ndust)
        for i,line in enumerate(f):
            if i==145:
                mmean = line
                numbermmean.append(mmean)
            if i>=200 and i <= 206:
                line = line.strip()
                line
                #print(line)
                columns = line.split()
                columns
                #print(columns)
                nt=0
                while nt <=7:
                    typedata = columns
                    nt += 1
                print('###### Typedata ########')  
                print(typedata)
                numbertypedata.append(typedata)

  
        '''if j > 0 and (float(mmean[0]) != float(mmean[j])):
        print("Ups! Your mean particle mass do not fit, there might be a problem")
        else:
        print("Great! Your mean particle mass fits! Go on!")'''
        j = j+1
    print('numbertypedata\n')
    print(numbertypedata)
    print('\n')
    
    
    
    
    ivec=0
    mrow=0
    while mrow <= 6*q:
        while ivec <= 4:
            if numbertypedata[mrow][ivec] == numbertypedata[mrow+7][ivec]:
                print('correct')
            else:
                print('problem')
                numbertypedata[mrow][ivec] = int(numbertypedata[mrow][ivec]) + int(numbertypedata[mrow+7][ivec])
                numbertypedata[mrow+7][ivec]= numbertypedata[mrow][ivec]
                str(numbertypedata[mrow][ivec])
                str(numbertypedata[mrow+7][ivec])
            ivec+=1    
        ivec=0
        mrow+=1  
    print(numbertypedata)  
    #for mrow in range(7):
    #    numbertypedata[mrow] = [str(x) for x in numbertypedata[mrow]]
    #    for ivec in range(5):
    #        numbertypedata[ivec] = '{:>10}'.format(numbertypedata[ivec]
    #    numbertypedata[mrow] = sum(numbertypedata[ivec]) 
    print(str(numbertypedata[0]))
    
    
    #numbertypedata[
    
    
    
     #       i = i+1
    allpaths.append(numberNhydro)
    allpaths.append(numberNstar)
    allpaths.append(numberNgas)
    allpaths.append(numberNcdm)
    allpaths.append(numberNdust)
    allpaths.append(numbermmean)
    allpaths.append(numbertypedata)
    

    #for line in allpaths:
    #    print(repr(line))
    
    print(allpaths)
    #print(float(allpaths[2][0]))
    #print('Particle number: ',float(allpaths[2][0]))
    kq=0
    print('kq = ',kq)
    print('j = ',j)
    while kq < j:
        sum_Nhydro = sum_Nhydro + int(allpaths[2][kq])
        sum_Ngas = sum_Ngas + int(allpaths[4][kq])
        sum_Ndust = sum_Ndust + int(allpaths[6][kq])
        kq = kq+1
    print('Sum of all Nhydro particles: ',sum_Nhydro)
    print('Sum of all Ngas particles: ',sum_Ngas)
    print('Sum of all Ndust particles: ',sum_Ndust)
    
    #for q in numbertypedata:
    #    numbertypedata = [ int(x) for x in numbertypedata[q] ]
    #    print(numbertypedata[q][:2])
    #    print(str(sum_Nhydro))
    #    print(numbertypedata[q][3:5])
    #sum_Nhydro = str(sum_Nhydro)
    #sum_Ngas = str(sum_Ngas)
    #sum_Ndust = str(sum_Ndust)
    #merged_Nhydro = np.arange(1,sum_Nhydro)#make a list of number of the sum
    #print(merged_Nhydro)
    mf = open(me_fullpath, 'w+')
    mf.write('SERENASCIIDUMPV2\n')  #format_id
    mf.write(header_pr)   #pr : Floating point precision (4 = single precision, 8 = double precision)
    mf.write(header_ndim) #ndim : Spatial dimensionality
    mf.write(header_vdim) #vdim : Velocity dimensionality
    mf.write(header_bdim) #bdim : Magnetic field dimensionality
   #idata[50] integer variables
    mf.write(str(sum_Nhydro))    # idata[0] = Nhydro : No. of hydro particles (SEREN = pgas)
    mf.write('\n         0\n')           # idata[1] = Nstar : No. of star/sink particles (SEREN = stot)
    mf.write('{0:10d}'.format(0))           # idata[2] = N/A in GANDALF (SEREN = pboundary : No. of static boundary particles)
    mf.write('\n')
    mf.write('{0:10d}'.format(0))           # idata[3] = N/A in GANDALF (SEREN = picm: No. of 'intercloud medium' particles)
    mf.write('\n')
    mf.write(str(sum_Ngas))    # idata[4] = Ngas : No. of self-gravitating gas particles (SEREN = pgas)
    mf.write('\n')
    mf.write(Ncdm)     # idata[5] = Ncdm : No. of self-gravitating cdm particles (SEREN = pcdm)
    mf.write(str(sum_Ndust))    # idata[6] = Ndust : No. of dust particles (SEREN = pdust)
    mf.write('\n         0\n')           # idata[7] = N/A in GANDALF (SEREN = pion : No. of particles)
    while zero < 12:
        mf.write('{0:10d}'.format(0))
        mf.write('\n')
        zero += 1
    zero=0
    mf.write('{0:10d}'.format(7))#nunit)         # idata[19] = nunit : No. of unit variables in header
    mf.write('\n')
    mf.write('{0:10d}'.format(0))#ndata)         # idata[20] = ndata : No. of data arrays in snapshot file
    mf.write('\n')
    #zeros(29)
    while zero < 28:
        mf.write('{0:10d}'.format(0))
        mf.write('\n')
        zero += 1
    zero=0
    #mf.write(str(np.zeros(29)))
    
    #ilpdata[50] : Long integer variables
    mf.write('{0:10d}'.format(1))#Noutsnap)    # ilpdata[0] = Noutsnap : No. of snapshot files created (SEREN = snapshot)
    mf.write('\n')
    mf.write('{0:10d}'.format(0))#Nsteps)      # ilpdata[1] = Nsteps : No. of complete integration steps (SEREN = nsteps)
    mf.write('\n')
    mf.write('{0:10d}'.format(0))         # ilpdata[2] = N/A in GANDALF (SEREN = ntempnext : Integer time for next temporary snapshot)
    mf.write('\n')
    mf.write('{0:10d}'.format(0))         # ilpdata[3] = N/A in GANDALF (SEREN = ndiagnext : Integer time for next diagnostic output)
    mf.write('\n')
    mf.write('{0:10d}'.format(0))         # ilpdata[4] = N/A in GANDALF (SEREN = nsnapnext : Integer time for next integer snapshot)
    mf.write('\n')
    mf.write('{0:10d}'.format(0))         # ilpdata[5] = N/A in GANDALF (SEREN = nsinknext : Integer time for next sink output)
    mf.write('\n')
    while zero < 4:
        mf.write('{0:10d}'.format(0))
        mf.write('\n')
        zero += 1
    zero=0
    #mf.write(str(np.zeros(4)))
    mf.write('         0\n')#Noutlitesnap)    # ilpdata[10] = Noutlitesnap : No. of lite snapshots (N/A in SEREN)
    while zero < 39:
        mf.write('         0\n')
        zero += 1
    zero=0
    #mf.write(str(np.zeros(39)))
    
    #rdata[50] : Standard precision floating-point variables
    mf.write('{:>.10e}'.format(1.2))#h fac)  # rdata[0] = h fac : 'No. of particles per smoothing length' factor in h-rho iteration (SEREN = h fac)
    mf.write('\n')
    mf.write('{:>.10e}'.format(0))    # rdata[1] = N/A in GANDALF (SEREN = gamma : Ratio of specific heats for gas)
    mf.write('\n')
    mf.write('{:>.10e}'.format(0))    # rdata[2] = N/A in GANDALF (SEREN = mu bar : Mean gas particle mass (in units of m h ))
    mf.write('\n')
    mf.write('{:>.10e}'.format(0))    # rdata[3] = N/A in GANDALF (SEREN = hmin : Minimum smoothing length)
    mf.write('\n')
    while zero < 46:
        mf.write('{:>.10e}'.format(0))
        mf.write('\n')
        zero += 1
    zero=0
    #mf.write(str(np.zeros(36)))
    
    #ddata[50] : Double precision floating-point variables
    mf.write('{:>.10e}'.format(0))#t)                # ddata[0] = t : Simulation time when snapshot was created (SEREN = time)
    mf.write('\n')
    mf.write('{:>.10e}'.format(0))#tsnaplast)        # ddata[1] = tsnaplast : Time that previous snapshot was created (SEREN = lastsnap)
    mf.write('\n')
    mf.write(numbermmean[0])          # ddata[2] = mmean : Average mass of gas particles (SEREN = mgas orig)
    while zero < 7:
        mf.write('{:>.10e}'.format(0))
        mf.write('\n')
        zero += 1
    zero=0
    #mf.write(str(np.zeros(7)))
    mf.write('0\n')#tlitesnaplast)    # ddata[10] = tlitesnaplast : Time when previous lite snapshot was created (N/A in SEREN)
    while zero < 39:
        mf.write('{:>.10e}'.format(0))
        mf.write('\n')
        zero += 1
    zero=0
    #mf.write(str(np.zeros(39)))
    
    #unit data[nunit]
    #data id[ndata] :
    mf.write('porig\n')    # porig : Original (unique) particle ids
    mf.write('r\n')        # r : Hydro particle positions
    mf.write('m\n')        # m : Hydro particle masses
    mf.write('h\n')        # h : Hydro particle smoothing lengths
    mf.write('v\n')        # v : Hydro particle velocities
    mf.write('rho\n')      # rho : Hydro particle densities
    mf.write('u\n')        # u : Hydro particle specific internal energies
    # sink v1
    
    #mf.write('\n')
    
    #-----------------------------------------------------------------------
    # typedata vectors
    '''td=0
    tdvector=[]
    sumtdvector=0
    while td <= 6:
        for i in range(5):
            tdvector.append('{:>10}'.format(numbertypedata[td][i]))
            sumtdvector = tdvector[i] + tdvector[i+1] + tdvector[i+2] + tdvector[i+3] + tdvector[i+4] + tdvector[i+5]
        mf.write(str(sumtdvector))
        print(sumtdvector)
        td += 1'''
    
    
    td=0
    i=0
    stdvector=[]
    for td in range(7):
        for i in range(5):
            stdvector.append('{:>10}'.format(numbertypedata[td][i]))
    sumtd1vector = stdvector[0] + stdvector[1] + stdvector[2] + stdvector[3] + stdvector[4]
    sumtd2vector = stdvector[5] + stdvector[6] + stdvector[7] + stdvector[8] + stdvector[9]
    sumtd3vector = stdvector[10] + stdvector[11] + stdvector[12] + stdvector[13] + stdvector[14]
    sumtd4vector = stdvector[15] + stdvector[16] + stdvector[17] + stdvector[18] + stdvector[19]
    sumtd5vector = stdvector[20] + stdvector[21] + stdvector[22] + stdvector[23] + stdvector[24]
    sumtd6vector = stdvector[25] + stdvector[26] + stdvector[27] + stdvector[28] + stdvector[29]
    sumtd7vector = stdvector[30] + stdvector[31] + stdvector[32] + stdvector[33] + stdvector[34]
    
    print(sumtd1vector)
    print(sumtd2vector)
    print(sumtd3vector)
    print(sumtd4vector)
    print(sumtd5vector)
    print(sumtd6vector)
    print(sumtd7vector)
    mf.write(sumtd1vector)
    mf.write('\n')
    mf.write(sumtd2vector)
    mf.write('\n')
    mf.write(sumtd3vector)
    mf.write('\n')
    mf.write(sumtd4vector)
    mf.write('\n')
    mf.write(sumtd5vector)
    mf.write('\n')
    mf.write(sumtd6vector)
    mf.write('\n')
    mf.write(sumtd7vector)
    mf.write('\n')
    
    # typedata vectors    
    #-----------------------------------------------------------------------

    
    iterate=0
    while iterate < sum_Nhydro:
        mf.write(str(iterate))
        mf.write('\n')
        iterate += 1
    
    # Let's start with the vector main stuff!
    i=0
    p=1
    m=0
    iNhydro = 0
    while p <= 6:
        n=0
        while n <= q:
            filename = str(allpaths[1][n])
            tmf = open(filename,'r+')
            Nhydro = (allpaths[2][n])
            print(Nhydro)
            i = int(Nhydro)*(p) + 219
            print(i)
            iNhydro = i + int(Nhydro)
            m = i
            for m,line in enumerate(tmf):
                if m >= i and m < (i+int(Nhydro)):
                    #print(line)
                    line = line.strip()
                    line
                    columns = line.split()
                    columns
                    #print(line)
                    mf.write(line)
                    mf.write('\n')       
                m += 1
            n += 1
        p += 1
            
    #np.arange(sum_Nhydro)
    #mf.write(np.arange(sum_Nhydro))
    #for #loop over all files and all rest entries
    mf.close()
    #mf.write(largest file)
    #mf.write iterate sum of all particles
    # loop for k < 6? (number of sections in the SERENfile
    # loop over all number of files
    #  mf.write always the number of particles and than switch to next file 
    
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
number_IC()
print('\n')
allpaths = findPath()
print'---------------'
print(allpaths)
print'---------------'
merge()
