import re
import sys

if len(sys.argv)<2:
    print('POSCAR File is not passed')
    sys.exit()

procar = open(sys.argv[1])
lines = procar.readlines()

#Extract data regarding kpoints, nbands and nions
n_kpoints = re.findall('\d+',lines[1])[0]
n_bands = re.findall('\d+',lines[1])[1]
n_ions = re.findall('\d+',lines[1])[2]

print('Number of Kpoints:'+n_kpoints)
print('Number of Bands:'+n_bands)
print('Number of Ions:'+n_ions)



