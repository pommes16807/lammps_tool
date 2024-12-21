import numpy as np

xyz_file_path="C:\\cygwin_wm\\home\\lammps\\python\\mp_1143_Al2O3.xyz"
output_path="C:\\cygwin_wm\\home\\lammps\\python\\mp_1143_Al2O3.dat"
comment_str="Lammps data file: converted from .xyz data."


Num_to_Atoms_Dic={1:"Al",2:"O"}
#Atom_Name_to_Num_Dic={"Al":1,"O":2}
Atom_Name_to_Num_Dic = {value: key for key, value in Num_to_Atoms_Dic.items()}
Atom_Name_to_Charges_Dic={"Al":0.000000,"O":0.000000}
Masses_dic={"Al":26.981539,"O":15.999400}

number_of_atoms_type=len(Num_to_Atoms_Dic)

number_of_atoms=0 # it is automatically calculated from .xyz data
xlow_ylow_z_low=[0,0,0] #it is outomatically calculated from .xyz data
xhi_y_hi_z_hi=[0,0,0]   #it is outomatically calculated from .xyz data

with open(xyz_file_path) as f:
    data_list = f.readlines()

data_list_xyz=[]
data_list_atom_name=[]
for i in range(2,len(data_list)):
    data_list_atom_name.append((data_list[i].split())[0])
    data_list_xyz.append((data_list[i].split())[1:])

data_x=np.zeros(len(data_list_xyz))
data_y=np.zeros(len(data_list_xyz))
data_z=np.zeros(len(data_list_xyz))


for i in range(len(data_list_xyz)):
    data_x[i]=float(data_list_xyz[i][0])
    data_y[i]=float(data_list_xyz[i][1])
    data_z[i]=float(data_list_xyz[i][2])






number_of_atoms=data_list[0]
comment_str=comment_str+":"+data_list[1]
count=1

output_str_all=""
output_str_all=output_str_all+comment_str
output_str_all=output_str_all+str(int(number_of_atoms))+" atoms\n"
output_str_all=output_str_all+str(int(number_of_atoms_type))+" atom types"+"\n"

#xlo xhi
output_str_all=output_str_all+ str(np.amin(data_x))+" " +str(np.amax(data_x))+" "+"xlo " + "xhi"+"\n"
output_str_all=output_str_all+ str(np.amin(data_y))+" " +str(np.amax(data_y))+" "+"ylo " + "yhi"+"\n"
output_str_all=output_str_all+ str(np.amin(data_z))+" " +str(np.amax(data_z))+" "+"zlo " + "zhi"+"\n"

#Pair coeff
COMMENT_PLUS="#"
output_str_all=output_str_all+"\n#Pair Coeffs"+"\n"
output_str_all=output_str_all+"#"+"\n"
for i in Num_to_Atoms_Dic:
    output_str_all=output_str_all+COMMENT_PLUS+str(i)+" "+Num_to_Atoms_Dic[i]+"\n"

#Masses
output_str_all=output_str_all+"\nMasses"+"\n\n"
for i in Num_to_Atoms_Dic:
    output_str_all=output_str_all+str(i)+" "+str(Masses_dic[Num_to_Atoms_Dic[i]])+"\n"


#xyz 
count=1
output_str_all=output_str_all+"\nAtoms\n\n"
for i in range(len(data_x)):
    output_str_all=output_str_all+str(count)+" "+str(Atom_Name_to_Num_Dic[data_list_atom_name[i]])+" "
    output_str_all=output_str_all+'{:.7f}'.format(Atom_Name_to_Charges_Dic[data_list_atom_name[i]])+" "
    output_str_all=output_str_all+'{:.7f}'.format(data_x[i])+" "
    output_str_all=output_str_all+'{:.7f}'.format(data_y[i])+" "
    output_str_all=output_str_all+'{:.7f}'.format(data_z[i])+"\n"
    count=count+1
print(output_str_all)

with open(output_path, mode='w') as f:
    f.write(output_str_all)