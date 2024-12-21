import re


file_lammps_trj="C:\\cygwin_wm\\home\\lammps\\python\\dump1.lammpstrj"


with open(file_lammps_trj) as f:
    data = f.read()



print("match:\n")
match = re.search(r"ITEM: NUMBER OF ATOMS\s+(\d+)", data)
if match: 
    number_of_atoms = match.group(1) 
    print(number_of_atoms)


pattern = rf'ITEM: ATOMS id type xs ys zs\n((?:.*\n){{{number_of_atoms}}})' 
match = re.findall(pattern, data) 
if match: 
    print(len(match) )
    for i in range(len(match)):
        print(i,match[i])
else:
    print("None") 