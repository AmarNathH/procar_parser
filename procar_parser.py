import re
import sys
import os
import shutil

if len(sys.argv)<2:
    print('Less number of arguments. Please pass the POSCAR file !')
    sys.exit()

if os.path.exists("Output"):
    print('Deleting old Output files')
    shutil.rmtree("Output")

procar = open(sys.argv[1])
lines = procar.readlines()

#Extract data regarding kpoints, nbands and nions
n_kpoints = re.findall('\d+',lines[1])[0]
n_bands = re.findall('\d+',lines[1])[1]
n_ions = re.findall('\d+',lines[1])[2]

print('Number of Kpoints:'+n_kpoints)
print('Number of Bands:'+n_bands)
print('Number of Ions:'+n_ions)

#Converting the values from string to integers
n_kpoints = int(n_kpoints)
n_bands = int(n_bands)
n_ions = int(n_ions)


band_data_space = n_ions + 5
kpoint_data_space = n_bands*band_data_space + 3

i_k = 4-1   #line number from where the k-point table starts
i_b = 2     #line number from where the band table starts
i_t = 7     #line number for the title of the table

#arrays to store poscar data
poscar_data = [[[ 0 for i in range(n_ions)] for j in range(n_bands)] for k in range(n_kpoints)] 

#generate files to store data
for c in range(n_ions):
    os.makedirs("Output/ion"+str(c+1))

#write data
for c in range(n_ions):
    for b in range(n_bands):
        flag = 1
        for a in range(n_kpoints):
            poscar_data[a][b][c] = str(a+1) + "\t" + lines[i_k + a*kpoint_data_space + i_b + b*band_data_space + 3 + c]
            files = open("Output/ion"+str(c+1)+"/band_{}".format(b+1),'a')

            if flag:
                files.write("kpoint\t" + lines[i_t])
                flag = 0

            files.write(poscar_data[a][b][c])
            files.close()    


#Loop to generate band_combined file for each ions
for c in range(n_ions):
    flag = 1
    for b in range(n_bands):

        for a in range(n_kpoints):
            poscar_data[a][b][c] = str(a+1)+ "\t"+ lines[i_k + a*kpoint_data_space + i_b + b*band_data_space + 3 + c]
            files = open("Output/ion"+str(c+1)+"/band_combined",'a')

            if flag:
                files.write("kpoint\t" + lines[i_t])

            files.write(poscar_data[a][b][c])
            files.close()
            flag = 0
    





