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
    #
    motion_choice = raw_input("Change the motion of gas? ((Y)es,1,(y)es)")
    if motion_choice == 'Y' or motion_choice == '1' or motion_choice == 'y':
        x_motion = float(input('Motion in X direction: '))
        y_motion = float(input('Motion in Y direction: '))
        z_motion = float(input('Motion in Z direction: '))
    star_choice = raw_input("Changes also for star? (0 = same as gas (no changes available), 1 = only position, 2 = only velocities, 3 = both, 4 = import stars/sinks")
    
    if star_choice == '0':
        x_star = x_dist
        y_star = y_dist
        z_star = z_dist
        xv_star = x_motion
        yv_star = y_motion
        zv_star = z_motion
    elif star_choice == '1':
        x_star = float(input('Starcluster position in X direction: '))
        y_star = float(input('Starcluster position in Y direction: '))
        z_star = float(input('Starcluster position in Z direction: '))
    elif star_choice == '2':
        xv_star = float(input('Starcluster Motion in X direction: '))
        yv_star = float(input('Starcluster Motion in Y direction: '))
        zv_star = float(input('Starcluster Motion in Z direction: '))
    elif star_choice == '3':
        x_star = float(input('Starcluster position in X direction: '))
        y_star = float(input('Starcluster position in Y direction: '))
        z_star = float(input('Starcluster position in Z direction: '))
        xv_star = float(input('Starcluster Motion in X direction: '))
        yv_star = float(input('Starcluster Motion in Y direction: '))
        zv_star = float(input('Starcluster Motion in Z direction: '))
    elif star_choice == '4':
        print('Please prepare a file with the following columns (position and velocity vectors in cartesian coordiantes in 3D:')
        print('| x | y | z | vx | vy | vz |')
        #import_ext_stars = raw_input('Path to external stars/sink file: ')
        
        
        #x_motion = '{:>.10e}'.format(x_motion)
        #print('x_motion = ',x_motion)
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
    Nstar = f.readline()
    pboundary = f.readline()
    picm = f.readline()
    Ngas = f.readline()
    Ncdm = f.readline()
    Ndust = f.readline()
    nf.write(header_formatID)
    #nf.write('\n')
    print('--- Shifted New File ---')
    print(header_formatID)
    nf.write(header_pr)
    #nf.write('\n')
    print(header_pr)
    nf.write(header_ndim)
    #nf.write('\n')
    print(header_ndim)
    nf.write(header_vdim)
    #nf.write('\n')
    print(header_vdim)
    nf.write(header_bdim)
    #nf.write('\n')
    print(header_bdim)
    nf.write(Nhydro)
    #nf.write('\n')
    print(Nhydro)
    #nf.write(Nstar)
    #data = []
    nf.write(Nstar)
    print(Nstar)
    nf.write(pboundary)
    print(pboundary)
    nf.write(picm)
    print(picm)
    nf.write(Ngas)
    print(Ngas)
    nf.write(Ncdm)
    print(Ncdm)
    nf.write(Ndust)
    print(Ndust)
    NHydro = Nhydro
    print(NHydro)
    print(Nhydro)
    int(Nhydro)
    if int(Nstar) > 0:
        i = int(Nhydro) + 209
    else:
        i = int(Nhydro) + 207 #where the position vector starts, see GANDALF docs SEREN format
    int(i)
    print(i)
    end_vec = int(i) + int(Nhydro) # 6 lines more than needed
    end_vec2 = end_vec + 1*int(Nhydro)
    end_vec3 = end_vec + 2*int(Nhydro)
    end_vec4 = end_vec + 3*int(Nhydro)
    end_vec5 = end_vec + 4*int(Nhydro)
    end_vec6 = end_vec + 5*int(Nhydro)

    print(end_vec)
    for m,line in enumerate(f):
        print('just m = ',m)
        if m < i:
            line = line.strip('\n')
            line
            #columns = line.split()
            #columns
            nf.write(line)
            nf.write('\n')
            print('line = ',line)
 #   for k,line in enumerate(f):
   #------------------------------
   # Changing the position vector:
   #------------------------------
        if m >= i and m < end_vec:# and k < end_vec:
            line = line.strip()
            line
            print('Position line = ',line)
            columns = line.split()
            columns
            if x_dist != 0 and y_dist != 0 and z_dist != 0:
                columns[0] = float(columns[0]) + x_dist
                columns[1] = float(columns[1]) + y_dist
                columns[2] = float(columns[2]) + z_dist
                columns[0] = '{:.10e}'.format(columns[0])
                columns[1] = '{:.10e}'.format(columns[1])
                columns[2] = '{:.10e}'.format(columns[2])
                new_line = columns[0] + '   ' + columns[1] + '   ' + columns[2] # adding format style!? instead of whitespace str
                nf.write(str(new_line))
                print(new_line)
                nf.write('\n')
                #print(columns[1])
                #print(columns[2])
            elif x_dist != 0 and y_dist != 0:
                columns[0] = float(columns[0]) + x_dist
                columns[1] = float(columns[1]) + y_dist
                columns[0] = '{:.10e}'.format(columns[0])
                columns[1] = '{:.10e}'.format(columns[1])
                columns[2] = str(columns[2])
                new_line = columns[0] + '   ' + columns[1] + '   ' + columns[2]
                nf.write(str(new_line))
                print(new_line)
                nf.write('\n')
                #print(columns)
            elif x_dist != 0 and z_dist != 0:
                columns[0] = float(columns[0]) + x_dist
                columns[2] = float(columns[2]) + z_dist
                columns[0] = '{:.10e}'.format(columns[0])
                columns[1] = str(columns[1])
                columns[2] = '{:.10e}'.format(columns[2])
                new_line = columns[0] + '   ' + columns[1] + '   ' + columns[2]
                nf.write(str(new_line))
                print(new_line)
                nf.write('\n')
                #print(columns)
            elif y_dist != 0 and z_dist != 0:
                columns[1] = float(columns[1]) + y_dist
                columns[2] = float(columns[2]) + z_dist
                columns[0] = str(columns[0])
                columns[1] = '{:.10e}'.format(columns[1])
                columns[2] = '{:.10e}'.format(columns[2])
                new_line = columns[0] + '   ' + columns[1] + '   ' + columns[2]
                nf.write(str(new_line))
                print(new_line)
                nf.write('\n')
                #print(columns)
            elif z_dist != 0:
                columns[2] = float(columns[2]) + z_dist
                columns[0] = str(columns[0])
                columns[1] = str(columns[1])
                columns[2] = '{:.10e}'.format(columns[2])
                new_line = columns[0] + '   ' + columns[1] + '   ' + columns[2]
                nf.write(str(new_line))
                print(new_line)
                nf.write('\n')
            elif y_dist != 0:
                columns[1] = float(columns[1]) + y_dist
                columns[0] = str(columns[0])
                columns[1] = '{:.10e}'.format(columns[1])
                columns[2] = str(columns[2])
                new_line = columns[0] + '   ' + columns[1] + '   ' + columns[2]
                nf.write(str(new_line))
                print(new_line)
                nf.write('\n')
            elif x_dist != 0:
                columns[0] = float(columns[0]) + x_dist
                columns[0] = '{:.10e}'.format(columns[0])
                columns[1] = str(columns[1])
                columns[2] = str(columns[2])
                new_line = columns[0] + '   ' + columns[1] + '   ' + columns[2]
                nf.write(str(new_line))
                print(new_line)
                nf.write('\n')
                
        
    #---------------------------
    # Adding the m and h vectors
    #---------------------------
           
        if m >= end_vec and m < end_vec3:
            line = line.strip()
            line
            columns = line.split()
            columns
            nf.write(line)
            print(line)
            nf.write('\n')
        
        
   #----------------------------------
   # Changing the motion vector block:
   #----------------------------------
   
        print('3*endvec = ',end_vec3)
        print('4*endvec = ',end_vec4)
        if m >= end_vec3 and m < end_vec4:# and motion_choice == 'Y' or motion_choice == '1' or motion_choice == 'y':
            line = line.strip()
            line
            print('m = ',m)
            print('motion_vec = ',line)
            columns = line.split()
            columns
            if x_motion != 0 and y_motion != 0 and z_motion != 0:
                columns[0] = float(columns[0]) + x_motion
                columns[1] = float(columns[1]) + y_motion
                columns[2] = float(columns[2]) + z_motion
                columns[0] = '{:.10e}'.format(columns[0])
                columns[1] = '{:.10e}'.format(columns[1])
                columns[2] = '{:.10e}'.format(columns[2])
                new_line = columns[0] + '   ' + columns[1] + '   ' + columns[2] # adding format style!? instead of whitespace str
                nf.write(str(new_line))
                print(new_line)
                nf.write('\n')
                #print(columns[1])
                #print(columns[2])
            elif x_motion != 0 and y_motion != 0:
                columns[0] = float(columns[0]) + x_motion
                columns[1] = float(columns[1]) + y_motion
                columns[0] = '{:.10e}'.format(columns[0])
                columns[1] = '{:.10e}'.format(columns[1])
                columns[2] = str(columns[2])
                new_line = columns[0] + '   ' + columns[1] + '   ' + columns[2]
                nf.write(str(new_line))
                print(new_line)
                nf.write('\n')
                #print(columns)
            elif x_motion != 0 and z_motion != 0:
                columns[0] = float(columns[0]) + x_motion
                columns[2] = float(columns[2]) + z_motion
                columns[0] = '{:.10e}'.format(columns[0])
                columns[1] = str(columns[1])
                columns[2] = '{:.10e}'.format(columns[2])
                new_line = columns[0] + '   ' + columns[1] + '   ' + columns[2]
                nf.write(str(new_line))
                print(new_line)
                nf.write('\n')
                #print(columns)
            elif y_motion != 0 and z_motion != 0:
                columns[1] = float(columns[1]) + y_motion
                columns[2] = float(columns[2]) + z_motion
                columns[0] = str(columns[0])
                columns[1] = '{:.10e}'.format(columns[1])
                columns[2] = '{:.10e}'.format(columns[2])
                new_line = columns[0] + '   ' + columns[1] + '   ' + columns[2]
                nf.write(str(new_line))
                print(new_line)
                nf.write('\n')
                #print(columns)
            elif z_motion != 0:
                columns[2] = float(columns[2]) + z_motion
                columns[0] = str(columns[0])
                columns[1] = str(columns[1])
                columns[2] = '{:.10e}'.format(columns[2])
                new_line = columns[0] + '   ' + columns[1] + '   ' + columns[2]
                nf.write(str(new_line))
                print(new_line)
                nf.write('\n')
            elif y_motion != 0:
                columns[1] = float(columns[1]) + y_motion
                columns[0] = str(columns[0])
                columns[1] = '{:.10e}'.format(columns[1])
                columns[2] = str(columns[2])
                new_line = columns[0] + '   ' + columns[1] + '   ' + columns[2]
                nf.write(str(new_line))
                print(new_line)
                nf.write('\n')
            elif x_motion != 0:
                print(columns)
                columns[0] = float(columns[0]) + x_motion
                columns[0] = '{:.10e}'.format(columns[0])
                columns[1] = str(columns[1])
                columns[2] = str(columns[2])
                new_line = columns[0] + '   ' + columns[1] + '   ' + columns[2]
                nf.write(str(new_line))
                print(new_line)
                nf.write('\n')
                
                

        #---------------
        # Adding the rho
        #---------------
           
        if m >= end_vec4 and m < end_vec5:
            line = line.strip()
            line
            columns = line.split()
            columns
            nf.write(line)
            print(line)
            nf.write('\n')
          
        #---------------------
        # Adding the u vectors
        #---------------------
        
        if m >= end_vec5 and m < end_vec6:
            line = line.strip()
            line
            columns = line.split()
            columns
            nf.write(line)
            print(line)
            nf.write('\n')
            
        #--------------------------------
        # Change star distance and motion
        #--------------------------------        
            
        ###################################
        #
        # ADDING STAR SHIFT HERE, and change the line ende above
        #
        ###################################
        if m == (end_vec6-1):
            line
            sink_data_length = line
            print('sink_data_length = ',sink_data_length)
            nf.write(sink_data_length)
            nf.write('\n')
        if m > end_vec6:
            line = line.strip()
            line
            columns = line.split()
            columns
            nf.write(columns)
            print('Star/Sink Vector columns: ',columns)
            nf.write('\n')
            
            
            #algorithm for changes
    
    nf.close()
    f.close()
    print('New Filename with distances: x = ', x_dist, ' y = ', y_dist, ' z = ', z_dist, '\n', newfullpath,'\n')
    fullpath = newfullpath
    print('Newfullpath: ')
    print(newfullpath)
    print('+++++++++++++')
    print('Fullpath (should be same as newfullpath: ')
    print(fullpath)
    return newfullpath#, Nhydro


#-------------------------------------------------------------------------
# Get all object names and append it to the full path and put it in a list
# Also asks if the distance has to be changed (position vector)
#-------------------------------------------------------------------------
def get_objects(path):
    n_objects = input('How many objects from this path? ')
    n_objects = n_objects -1
    j=0
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
    return merge_list#fullpath#, Nhydro



#----------------------------------------
# Function to add the path to your object
#------------------------------------------------
# Asks for total number of Paths to loop through
# which will lead to ask for number of objects in 
# the current path to loop through
#------------------------------------------------
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
        #numberpaths.append(k)
        #numberfullpath.append(fullpath)
        #numberNhydro.append(Nhydro)
        allpaths=fullpath#[numberpaths,numberfullpath]#,numberNhydro]
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
        print(allpaths[:])
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
    print('---------------------')
    print('- Merging all files -')
    print('---------------------')
    allpaths[:]
    numberNhydro=[]
    numberNstar=[]
    numberNgas=[]
    numberNcdm=[]
    numberNdust=[]
    numbermmean=[]
    typedata=[]
    numbertypedata=[]
    NA=0
    zero=0
    mmean=0
    sum_Nhydro = 0
    sum_Nstar = 0
    sum_Ngas = 0
    sum_Ncdm = 0
    sum_Ndust = 0
    add_stars = raw_input('Do you want some stars from a datafile? (Y)es, 1, (y)es ')
    
    if add_stars == 'Y' or add_stars == '1' or add_stars == 'y':
        print('External star input file will be added here!')
        ext_star_n = input('How many star will be added: ')
        ext_star_path = raw_input('Path and filename for external stars file: ')
    print('allpaths = ',allpaths[:])
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
        header_formatID = f.readline() #0 | 0
        header_pr = f.readline()
        header_ndim = f.readline()
        header_vdim = f.readline()
        header_bdim = f.readline()
        Nhydro = f.readline() #0 | 5
        Nhydro = Nhydro.strip()
        Nstar = f.readline()
        Nstar = Nstar.strip()
        pboundary = f.readline()
        pboundary = pboundary.strip()
        picm = f.readline()
        picm = picm.strip()
        Ngas = f.readline()
        Ngas = Ngas.strip()
        Ncdm = f.readline()
        Ncdm = Ncdm.strip()
        Ndust = f.readline()
        Ndust = Ndust.strip()
        pion = f.readline() #7 | 12
        pion = pion.strip()
        while i < 11:
            NA = f.readline()
            i +=1
        i=0
        #for i in range(8,19):
        #    NA[i] = f.readline()
        nunit = f.readline() #19
        ndata = f.readline() #20
        print('ndata = ',ndata)
        while i < 7:
            NA = f.readline()
            i +=1
        i=0
        #for i in range(21,29):
        #    NA[i] = f.readline()
        dmdt_range = f.readline() #29
        pgas_orig = f.readline() #30
        pp_gather = f.readline() #31
        while i < 7:
            NA = f.readline()
            i +=1
        i=0
        #for i in range(32,39):
        #    NA[i] = f.readline()
        rank = f.readline() #39
        Nmpi = f.readline() #40
        while i < 10:
            NA = f.readline()
            print('NA i[',i,'] = ',NA)
            i +=1
        i=0
        #for i in range(41,51):
        #    NA[i] = f.readline()
        Noutsnap = f.readline() #0 | 51    
        print('Noutsnap = ',Noutsnap)
        Nsteps = f.readline()
        ntempnext = f.readline()        
        ndiagnext = f.readline()
        nsnapnext = f.readline()
        nsinknext = f.readline() #5 | 56
        while i < 3:
            NA = f.readline()
            i +=1
        i=0
        #for i in range(57,60):
        #    NA[i] = f.readline()        
        Noutlitesnap = f.readline() #10
        while i < 40:
            NA = f.readline()
            i +=1
        i=0
        #for i in range(61,101):
        #    NA[i] = f.readline()
        h_fac = f.readline() #0 | 101
        print('h_fac = ',h_fac)
        gamma = f.readline()
        mu_bar = f.readline()
        hmin = f.readline() #3 | 104
        while i < 46:
            NA = f.readline()
            i +=1
        i=0
        #for i in range(105,151):
        #    NA[i] = f.readline()
        t = f.readline() #0 | 151
        tsnaplast = f.readline()
        mmean = f.readline() #2 | 153
        print('mmean = ',mmean)
        while i < 6:
            NA = f.readline()
            i +=1
        i=0
        #for i in range(154,160):
        #    NA[i] = f.readline()        
        tlitesnaplast = f.readline() #10 | 160
        while i < 40:
            NA = f.readline()
            i +=1
        i=0
        #for i in range(161,201):
        #    NA[i] = f.readline()    
        
            
        numberNhydro.append(Nhydro)
        numberNstar.append(Nstar)
        numberNgas.append(Ngas)
        numberNcdm.append(Ncdm)
        numberNdust.append(Ndust)
        numbermmean.append(mmean)
        print('numberNhydro = ',numberNhydro)
        print('numberNstar = ',numberNstar)
        print('Ngas = ',Ngas)
        print('Ncdm = ',Ncdm)
        print('Ndust = ',Ndust)
        print('Nstar = ',Nstar)
        print('numbermmean = ',numbermmean)
        nunit_porig = f.readline()
        nunit_r = f.readline()
        nunit_m = f.readline()
        nunit_h = f.readline()
        nunit_v = f.readline()
        nunit_rho = f.readline()
        nunit_u = f.readline()
        if Nstar > 0:
            nunit_sink_v1 = f.readline()
        
        print('porig = ',nunit_porig)
        print('r = ',nunit_r)
        print('m = ',nunit_m)
        print('h = ',nunit_h)
        print('v = ',nunit_v)
        print('rho = ',nunit_rho)
        print('u = ',nunit_u)
        print('sink_v1 = ',nunit_sink_v1)
        np.array = f.readline()
        firstvec = np.array
        print('firstvector = ',firstvec)
        np.array = f.readline()
        secondvec = np.array
        print('secondvector = ',secondvec)
        np.array = f.readline()
        thirdvec = np.array
        print('thirdvector = ',thirdvec)
        np.array = f.readline()
        fourthvec = np.array
        print('fourthvector = ',fourthvec)
        np.array = f.readline()
        fifthvec = np.array
        print('fifthvector = ',fifthvec)
        np.array = f.readline()
        sixthvec = np.array
        print('sixthvector = ',sixthvec)
        np.array = f.readline()
        seventhvec = np.array
        print('seventhvector = ',seventhvec)
        if int(Nstar) > 0:
            np.array = f.readline()
            eightvec = np.array
            print('eightvector = ',eightvec)
        numbertypedata.append(firstvec)
        numbertypedata.append(secondvec)
        numbertypedata.append(thirdvec)
        numbertypedata.append(fourthvec)
        numbertypedata.append(fifthvec)
        numbertypedata.append(sixthvec)
        numbertypedata.append(seventhvec)
        if int(Nstar) > 0:
            numbertypedata.append(eightvec)
        j = j+1
        print('j = ',j)
        #j=j+1
    #numbertypedata
    p = numbertypedata
    line = p
    #line
    line1 = [elem.strip().split() for elem in line]
    np.array=line1
    numbertypedata = np.array
    if int(Nstar) > 0:
        hybrid = 8
    else:
        hybrid = 7
    check = 0
    for check in range(hybrid):
        if numbertypedata[check] == numbertypedata[check+hybrid]:
            print('Vectors OK')
        else:
            print('You shall not pass')


    allpaths.append(numberNhydro)
    allpaths.append(numberNstar)
    allpaths.append(numberNgas)
    allpaths.append(numberNcdm)
    allpaths.append(numberNdust)
    allpaths.append(numbermmean)
    allpaths.append(numbertypedata)
    print('numbertypedata = ',numbertypedata)
    
    
    print(allpaths)
    kq=0
    print('kq = ',kq)
    print('j = ',j)
    while kq < j:
        print('allpaths[2][kq] =', allpaths[2][kq])
        sum_Nhydro = sum_Nhydro + int(allpaths[2][kq])
        sum_Nstar = sum_Nstar + int(allpaths[3][kq])
        '''if ext_star_n > 0:
            sum_Nstar = sum_Nstar + int(ext_star_n)
        elif ext_star_n <= 0:
            print('You\'ve set the number of stars in the external file to zero or negative.')
            print('No external star file will be read!')'''
        
        sum_Ngas = sum_Ngas + int(allpaths[4][kq])
        sum_Ncdm = sum_Ncdm + int(allpaths[5][kq])
        sum_Ndust = sum_Ndust + int(allpaths[6][kq])
        kq = kq+1
    print('Sum of all Nhydro particles: ',sum_Nhydro)
    print('Sum of all Nstar particles:', sum_Nstar)
    print('Sum of all Ngas particles: ',sum_Ngas)
    print('Sum of all Ndust particles: ',sum_Ndust)
    
    
    ########################################################
    #                                                      #
    # Part to read in the merged files, in the right order #
    #                                                      #
    ########################################################
    
    mf = open(me_fullpath, 'w+')
    print('------- File Start here: --------')
    print('')
    print('SERENASCIIDUMPV2\n')
    mf.write('SERENASCIIDUMPV2\n')  #format_id
    mf.write(header_pr)   #pr : Floating point precision (4 = single precision, 8 = double precision)
    print(header_pr)
    mf.write(header_ndim) #ndim : Spatial dimensionality
    print(header_ndim)
    mf.write(header_vdim) #vdim : Velocity dimensionality
    print(header_vdim)
    mf.write(header_bdim) #bdim : Magnetic field dimensionality
    print(header_bdim)
   #idata[50] integer variables
    mf.write(str(sum_Nhydro))    # idata[0] = Nhydro : No. of hydro particles (SEREN = pgas)
    mf.write('\n')
    print(str(sum_Nhydro)) 
    mf.write(str(sum_Nstar))     # idata[1] = Nstar : No. of star/sink particles (SEREN = stot)
    mf.write('\n')
    print(str(sum_Nstar))
    mf.write(pboundary)           # idata[2] = N/A in GANDALF (SEREN = pboundary : No. of static boundary particles)
    mf.write('\n')
    print(pboundary) 
    mf.write(picm)           # idata[3] = N/A in GANDALF (SEREN = picm: No. of 'intercloud medium' particles)
    mf.write('\n')
    mf.write(str(sum_Ngas))    # idata[4] = Ngas : No. of self-gravitating gas particles (SEREN = pgas)
    mf.write('\n')
    print(str(sum_Ngas))
    mf.write(str(sum_Ncdm))     # idata[5] = Ncdm : No. of self-gravitating cdm particles (SEREN = pcdm)
    mf.write('\n')
    print(str(sum_Ncdm)) 
    mf.write(str(sum_Ndust))    # idata[6] = Ndust : No. of dust particles (SEREN = pdust)
    mf.write('\n')
    print(str(sum_Ndust))
    mf.write(pion)           # idata[7] = N/A in GANDALF (SEREN = pion : No. of particles)
    print(pion)
    mf.write('\n')
    while zero < 11:
        mf.write('{0:10d}'.format(0))
        
        mf.write('\n')
        zero += 1
    #for i in range(8,19):
    #    mf.write(NA[i])
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
    print(numbermmean[0]) 
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
    if int(Nstar) > 0:
        mf.write('sink_v1\n')# sink v1
    

    
    
    td=0
    i=0
    stdvector=[]
    if int(Nstar) > 0:
        hybrid=8
    else:
        hybrid=7
    for td in range(hybrid):
        for i in range(5):
            stdvector.append('{:>10}'.format(numbertypedata[td][i]))
            #print(stdvector)
    sumtd1vector = stdvector[0] + stdvector[1] + '{0:10d}'.format(sum_Ngas) +  stdvector[3] + stdvector[4]#stdvector[2]
    sumtd2vector = stdvector[5] + stdvector[6] + '{0:10d}'.format(sum_Ngas) + stdvector[8] + stdvector[9]#stdvector[7]
    sumtd3vector = stdvector[10] + stdvector[11] + '{0:10d}'.format(sum_Ngas) + stdvector[13] + stdvector[14]#stdvector[12]
    sumtd4vector = stdvector[15] + stdvector[16] + '{0:10d}'.format(sum_Ngas) + stdvector[18] + stdvector[19]#stdvector[17]
    sumtd5vector = stdvector[20] + stdvector[21] + '{0:10d}'.format(sum_Ngas) + stdvector[23] + stdvector[24]#stdvector[22]
    sumtd6vector = stdvector[25] + stdvector[26] + '{0:10d}'.format(sum_Ngas) + stdvector[28] + stdvector[29]#stdvector[27]
    sumtd7vector = stdvector[30] + stdvector[31] + '{0:10d}'.format(sum_Ngas) + stdvector[33] + stdvector[34]#stdvector[32]
    if int(Nstar) > 0:
        sumtd8vector = stdvector[35] + stdvector[36] + '{0:10d}'.format(sum_Nstar) + stdvector[38] + stdvector[39]
        
    print('sumtd1vector = ',sumtd1vector)
    print('sumtd2vector = ',sumtd2vector)
    print('sumtd3vector = ',sumtd3vector)
    print('sumtd4vector = ',sumtd4vector)
    print('sumtd5vector = ',sumtd5vector)
    print('sumtd6vector = ',sumtd6vector)
    print('sumtd7vector = ',sumtd7vector)
    if int(Nstar) > 0:
        print('sumtd8vector = ',sumtd8vector)
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
    if int(Nstar) > 0:
        mf.write(sumtd8vector)
        mf.write('\n')
    # typedata vectors    
    #-----------------------------------------------------------------------

    
    iterate=0
    while iterate < (sum_Nhydro):
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
            Nstar = (allpaths[3][n])
            print('Nhydro = ',Nhydro)
            print('Nstar = ',Nstar)
            if int(Nstar) > 0:
                intro_lines = 221
            else:
                intro_lines = 219
            i = int(Nhydro)*(p) + intro_lines
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
                    print('line: ',line)
                    mf.write('\n')       
                m += 1
            n += 1
        p += 1

    #------------------
    # Part adding stars
    #------------------
    i = i+int(Nhydro)
    star_sink_vec=[]
    #m = m + int(Nhydro)
    if sum_Nstar > 0:
        print('sum_Nstar = ',sum_Nstar)
        n = 0
    for m,line in enumerate(tmf):
        if m == i:
            line
            mf.write(line)

        while n <= q:
            filename = str(allpaths[1][n])
            tmf = open(filename,'r+')
            Nstar = (allpaths[3][n])
            print('Nstar = ',Nstar)
            print('m = ',m)
            count = 0
            for m,line in enumerate(tmf):
                #if m == i:
                #    line
                #    print('sink_v1 line = ',line)
                #    mf.write(line)
                if m > i:
                    line
                    line = line.strip()
                    columns
                    columns = line.split()
                    np.array = columns
                    star_sink_vec.append(np.array)
                    a = star_sink_vec
                    final = a
            n += 1
        if add_stars == True:
            print('add_stars will be added here!')
    
    
    count = 1
    j=1
    while count < (sum_Nstar+1):
        final[j][0] = str(count)
        j += 3
        count += 1
    j=0
    while j <= (sum_Nstar*3):
        print('final[',[j],'] = ',final[j])
        final1 = final[j]
        #final1 = final1.strip()
        print(final1)
        mf.write(str(final1))
        mf.write('\n')
        j += 1
        
    
    #print('final = ',final)
    #mf.write(final)
    
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
cmd = 'ls -al'
os.system(cmd)
number_IC()
print('\n')
allpaths = findPath()
print'---------------'
print(allpaths[:][:])
print'---------------'
merge()
